"""
AI Service for Sonship Analysis
Uses OpenAI API to analyze scripture through the lens of sonship theology
"""

from openai import OpenAI
from typing import Dict, Optional

class AIService:
    """Service for AI-powered scripture analysis"""
    
    def __init__(self):
        # OpenAI client is pre-configured via environment variables
        self.client = OpenAI()
        self.model = "gpt-4.1-mini"
        
        # Core sonship theology framework
        self.sonship_context = """
You are a Bible study assistant specializing in sonship theology. Sonship theology emphasizes the believer's identity as an adopted child of God with full inheritance rights and intimate relationship with the Father.

Key theological themes to emphasize:
1. ADOPTION: Believers are adopted into God's family (Romans 8:15, Galatians 4:5, Ephesians 1:5)
2. INHERITANCE: Co-heirs with Christ, receiving all the promises (Romans 8:17, Galatians 4:7)
3. INTIMACY: Abba, Father relationship - deep personal connection with God (Romans 8:15, Galatians 4:6)
4. IDENTITY: Who we are in Christ as children of God, not what we do
5. FREEDOM: From law, fear, condemnation, and orphan mindset (Galatians 4:7, Romans 8:1-2)
6. SPIRIT OF ADOPTION: The Holy Spirit testifies that we are God's children (Romans 8:16)
7. MATURITY: Growing from children to mature sons who reflect the Father (Ephesians 4:13-15)
8. CONTRAST: Spirit of adoption vs. spirit of slavery/fear (Romans 8:15)

Key scripture passages on sonship:
- Romans 8:14-17 (Led by Spirit, Abba Father, co-heirs)
- Galatians 4:4-7 (Adoption, no longer slaves, heirs)
- Ephesians 1:3-6 (Predestined for adoption, accepted in the Beloved)
- 1 John 3:1-2 (Behold what manner of love, we are children of God)
- John 1:12 (Right to become children of God)

When analyzing scripture:
- Always look for sonship themes and connections
- Explain how the passage relates to the believer's identity as God's child
- Show practical implications for living as a son/daughter of God
- Be encouraging and faith-building
- Maintain theological accuracy and biblical fidelity
- Use accessible language that helps people understand deep truths
"""
    
    def analyze_scripture(self, scripture_text: str, reference: str) -> Optional[str]:
        """
        Analyze scripture through the lens of sonship theology
        
        Args:
            scripture_text: The Bible verse(s) text
            reference: The scripture reference (e.g., "Romans 8:14-17")
        
        Returns:
            AI-generated sonship analysis or None if error
        """
        try:
            prompt = f"""
Analyze the following scripture passage through the lens of sonship theology:

Reference: {reference}
Text: {scripture_text}

Provide a thoughtful analysis that:
1. Identifies any direct or indirect sonship themes in the passage
2. Explains how this passage relates to our identity as God's children
3. Shows practical implications for living as sons/daughters of God
4. Connects to other key sonship passages if relevant
5. Provides encouraging, faith-building insights

Keep the response clear, accessible, and around 200-300 words.
"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.sonship_context},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"Error in AI analysis: {e}")
            return None
    
    def answer_question(self, scripture_text: str, reference: str, question: str) -> Optional[str]:
        """
        Answer a user's question about scripture from sonship perspective
        
        Args:
            scripture_text: The Bible verse(s) text
            reference: The scripture reference
            question: User's question
        
        Returns:
            AI-generated answer or None if error
        """
        try:
            prompt = f"""
Scripture Reference: {reference}
Scripture Text: {scripture_text}

User's Question: {question}

Answer the question from a sonship theology perspective. Be clear, biblical, and encouraging. Keep the response concise (150-250 words).
"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.sonship_context},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=400
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"Error answering question: {e}")
            return None
    
    def get_study_guide(self, topic: str) -> Optional[str]:
        """
        Generate a study guide on a sonship-related topic
        
        Args:
            topic: The topic to study (e.g., "adoption", "inheritance", "identity")
        
        Returns:
            AI-generated study guide or None if error
        """
        try:
            prompt = f"""
Create a brief Bible study guide on the sonship topic: "{topic}"

Include:
1. A short introduction to the topic (2-3 sentences)
2. 3-5 key scripture passages to study
3. Key insights and questions for reflection
4. Practical application for daily life

Keep it concise and actionable (300-400 words).
"""
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.sonship_context},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=600
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"Error generating study guide: {e}")
            return None
