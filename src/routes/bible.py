"""
Bible Study API Routes
"""

from flask import Blueprint, request, jsonify
from src.services.bible_service import BibleService
from src.services.ai_service import AIService

bible_bp = Blueprint('bible', __name__)

# Initialize services
bible_service = BibleService()
ai_service = AIService()

@bible_bp.route('/verse', methods=['GET'])
def get_verse():
    """
    Get a Bible verse by reference
    Query params: reference (required), translation (optional, default: kjv)
    Example: /api/verse?reference=John 3:16&translation=kjv
    """
    reference = request.args.get('reference')
    translation = request.args.get('translation', 'kjv')
    
    if not reference:
        return jsonify({"error": "Reference parameter is required"}), 400
    
    verse_data = bible_service.get_verse(reference, translation)
    
    if verse_data:
        return jsonify(verse_data), 200
    else:
        return jsonify({"error": "Could not fetch verse. Please check the reference."}), 404

@bible_bp.route('/chapter', methods=['GET'])
def get_chapter():
    """
    Get an entire chapter
    Query params: book (required), chapter (required), translation (optional)
    Example: /api/chapter?book=Romans&chapter=8&translation=kjv
    """
    book = request.args.get('book')
    chapter = request.args.get('chapter')
    translation = request.args.get('translation', 'kjv')
    
    if not book or not chapter:
        return jsonify({"error": "Book and chapter parameters are required"}), 400
    
    try:
        chapter_num = int(chapter)
        chapter_data = bible_service.get_chapter(book, chapter_num, translation)
        
        if chapter_data:
            return jsonify(chapter_data), 200
        else:
            return jsonify({"error": "Could not fetch chapter. Please check the reference."}), 404
    except ValueError:
        return jsonify({"error": "Chapter must be a number"}), 400

@bible_bp.route('/analyze', methods=['POST'])
def analyze_scripture():
    """
    Analyze scripture through sonship lens
    Body: { "reference": "Romans 8:14-17", "text": "verse text...", "translation": "kjv" }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    
    reference = data.get('reference')
    text = data.get('text')
    
    # If text not provided, fetch it
    if not text and reference:
        translation = data.get('translation', 'kjv')
        verse_data = bible_service.get_verse(reference, translation)
        if verse_data:
            text = verse_data['text']
            reference = verse_data['reference']
        else:
            return jsonify({"error": "Could not fetch verse for analysis"}), 404
    
    if not reference or not text:
        return jsonify({"error": "Reference and text are required"}), 400
    
    analysis = ai_service.analyze_scripture(text, reference)
    
    if analysis:
        return jsonify({
            "reference": reference,
            "text": text,
            "analysis": analysis
        }), 200
    else:
        return jsonify({"error": "Could not generate analysis"}), 500

@bible_bp.route('/ask', methods=['POST'])
def ask_question():
    """
    Ask a question about scripture
    Body: { "reference": "Romans 8:15", "text": "verse text...", "question": "What does Abba mean?" }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    
    reference = data.get('reference')
    text = data.get('text')
    question = data.get('question')
    
    # If text not provided, fetch it
    if not text and reference:
        translation = data.get('translation', 'kjv')
        verse_data = bible_service.get_verse(reference, translation)
        if verse_data:
            text = verse_data['text']
            reference = verse_data['reference']
    
    if not reference or not text or not question:
        return jsonify({"error": "Reference, text, and question are required"}), 400
    
    answer = ai_service.answer_question(text, reference, question)
    
    if answer:
        return jsonify({
            "reference": reference,
            "text": text,
            "question": question,
            "answer": answer
        }), 200
    else:
        return jsonify({"error": "Could not generate answer"}), 500

@bible_bp.route('/study', methods=['GET'])
def get_study_guide():
    """
    Get a study guide on a sonship topic
    Query params: topic (required)
    Example: /api/study?topic=adoption
    """
    topic = request.args.get('topic')
    
    if not topic:
        return jsonify({"error": "Topic parameter is required"}), 400
    
    study_guide = ai_service.get_study_guide(topic)
    
    if study_guide:
        return jsonify({
            "topic": topic,
            "content": study_guide
        }), 200
    else:
        return jsonify({"error": "Could not generate study guide"}), 500

@bible_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "Bible Study API"}), 200
