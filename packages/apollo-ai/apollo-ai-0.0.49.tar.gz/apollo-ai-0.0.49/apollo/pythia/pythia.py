import concurrent.futures
import difflib
import json
import logging
import multiprocessing
import os
import re
import time

import jiwer
import spacy
from epitran import Epitran
from faster_whisper import WhisperModel
from pyphen import Pyphen

from .utils import (
    transcribe_file,
    split_audio_into_chunks
)

logging.basicConfig(format='APOLLO: (%(asctime)s): %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def clean_text(text: str) -> str:
    try:
        cleaned_text = re.sub(r'[^A-Za-z0-9áéíóúÁÉÍÓÚñÑüÜ]+', ' ', text)
        data = {"data": cleaned_text}
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error getting clean text: {str(e)}"})


def sentences(text: str) -> str:
    try:
        sentence_delimiters = r'[.!?]|(?:\.{3})|…|¡|¿|;|"'
        spanish_prefixes = ['Sr.', 'Sra.', 'Dr.', 'Lic.', 'Ing.']

        for prefix in spanish_prefixes:
            text = text.replace(prefix, prefix.replace('.', '###'))

        sentences_ = re.split(sentence_delimiters, text)

        for prefix in spanish_prefixes:
            sentences_ = [sentence.replace(prefix.replace('.', '###'), prefix) for sentence in sentences_]

        processed_sentences = []
        for sentence in sentences_:
            sentence = sentence.strip()
            if sentence and not sentence.startswith("–") and not sentence.startswith("-"):
                sentence = sentence.strip(":").strip(", ")
                processed_sentences.append(sentence)

        data = {"data": processed_sentences}
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error getting sentences: {str(e)}"})


def word_checker(original_text: str, new_text: str) -> str:
    try:
        original_words = dict(json.loads(words(original_text, True)))["data"]
        new_words = dict(json.loads(words(new_text, True)))["data"]

        output = jiwer.process_words(dict(json.loads(clean_text(original_text)))["data"],
                                     dict(json.loads(clean_text(new_text)))["data"])

        wer = output.wer
        mer = output.mer
        wip = output.wip
        wil = output.wil

        correct_words = [word for word in original_words if word in new_words]
        omitted_words = [word for word in original_words if word not in new_words]
        incorrect_words = [word for word in new_words if word not in original_words]

        data = {
            "correct_words": correct_words,
            "omitted_words": omitted_words,
            "incorrect_words": incorrect_words,
            "mer": mer,
            "wil": wil,
            "wip": wip,
            "wer": wer
        }
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error comparing words: {str(e)}"})


def word_alignment(original_text: str, new_text: str) -> str:
    try:
        original_words = dict(json.loads(words(original_text)))["data"]
        new_words = dict(json.loads(words(new_text)))["data"]
        matcher = difflib.SequenceMatcher(None, original_words, new_words)
        alignment = []
        residual_words = []
        extra_words = []

        for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
            if opcode == 'equal':
                alignment.extend(original_words[a0:a1])
            elif opcode == 'delete':
                alignment.extend('+' * len(word) for word in original_words[a0:a1])
                residual_words.extend(original_words[a0:a1])
            elif opcode in ('insert', 'replace'):
                alignment.extend('*' * len(word) for word in new_words[b0:b1])
                extra_words.extend(new_words[b0:b1])

        data = {
            "alignment": alignment,
            "residual_words": residual_words,
            "extra_words": extra_words
        }
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error on word alignment: {str(e)}"})


def phonetic_transcription(text: str, lang='spa-Latn') -> str:
    epi = Epitran(lang)
    try:
        transcription = epi.transliterate(dict(json.loads(clean_text(text)))["data"])
        data = {"data": transcription}
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error getting the phonetic transcription: {str(e)}"})


def syllables(text: str, lang='es') -> str:
    nlp = spacy.load('es_core_news_lg' if lang == 'es' else 'en_core_web_lg')
    py_instance = Pyphen(lang=lang)
    try:
        text = dict(json.loads(clean_text(text)))["data"]
        doc = nlp(text)
        list_words = [token.text for token in doc]
        list_syllables = [syllable for word in list_words for syllable in py_instance.inserted(word).split('-')]

        data = {"data": list_syllables}
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error getting syllables: {str(e)}"})


def words(text: str, lower=False, lang='es') -> str:
    nlp = spacy.load('es_core_news_lg' if lang == 'es' else 'en_core_web_lg')
    try:
        text = dict(json.loads(clean_text(text)))["data"]
        doc = nlp(text.lower() if lower else text)
        list_words = [token.text for token in doc]

        data = {"data": list_words}
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error on getting words: {str(e)}"})


def transcriber_parallel(file: str, model_name='small', device='cpu', max_processes=0, compute_type='float16',
                         lang='es', silence_threshold: str = "-20dB", silence_duration: float = 2.0) -> str:
    if max_processes > multiprocessing.cpu_count() or max_processes == 0:
        max_processes = multiprocessing.cpu_count()

    temp_files_array = split_audio_into_chunks(file, max_processes, silence_threshold, silence_duration)
    model = WhisperModel(model_name, device=device, compute_type=compute_type, cpu_threads=4)
    segments_output = []
    futures = []

    try:
        logging.info("Starting transcription")
        start_time = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_processes) as executor:
            for file_path in temp_files_array:
                future = executor.submit(transcribe_file, file_path, model, lang)
                futures.append(future)

        transcription = ""
        for future in futures:
            segments = future.result()
            for segment in segments:
                segments_output.append(
                    {"start": segment.start, "end": segment.end, "text": segment.text, "words": segment.words}
                )
                transcription += segment.text + " "

        for temp_file in temp_files_array:
            os.remove(temp_file)

        data = {"transcription": transcription, "segments": segments_output, "time_taken": time.time() - start_time}
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error transcribing: {str(e)}"})


def transcriber(file: str, model_name='large-v2', device='cuda', compute_type='float16', beam_size=5, lang='es') -> str:
    model = WhisperModel(model_name, device=device, compute_type=compute_type)
    segments_output = []

    try:
        logging.info("Starting transcription")
        start_time = time.time()

        segments, info = model.transcribe(file, beam_size=beam_size, language=lang, word_timestamps=True)

        transcription = ""
        for segment in segments:
            segments_output.append(
                {"start": segment.start, "end": segment.end, "text": segment.text, "words": segment.words,
                 "tokens": segment.tokens}
            )
            transcription += segment.text + " "

        data = {"transcription": transcription, "segments": segments_output, "info": info,
                "time_taken": time.time() - start_time}
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": f"Error transcribing: {str(e)}"})
