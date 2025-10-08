# AI-Powered Bible Study App

An intelligent Bible study application that helps users understand scripture through the theological lens of **sonship** - the concept of believers as adopted children of God with full inheritance rights and intimate relationship with the Father.

## Features

### 📖 Scripture Search
Search and display Bible passages by reference (e.g., "John 3:16", "Romans 8:14-17"). Supports multiple translations including KJV, NIV, and ESV.

### ✨ AI-Powered Sonship Analysis
Get deep insights into scripture passages through the lens of sonship theology. The AI analyzes verses to reveal:
- Identity as God's children
- Inheritance and promises
- Intimacy with the Father (Abba)
- Freedom from orphan mindset
- Spirit of adoption vs. spirit of slavery
- Practical applications for daily life

### 📚 Interactive Study Guides
Generate comprehensive study guides on key sonship themes:
- **Adoption**: Understanding our position in God's family
- **Inheritance**: Co-heirs with Christ
- **Identity**: Who we are in Christ
- **Intimacy**: Abba, Father relationship
- **Freedom**: From law, fear, and condemnation
- **Maturity**: Growing as sons and daughters of God

### 💬 Ask Questions
Ask specific questions about scripture passages and receive answers from a sonship perspective.

## Technology Stack

### Backend
- **Flask**: Python web framework for RESTful API
- **OpenAI API**: GPT-4.1-mini for AI-powered analysis
- **Bible API**: Free Bible verse retrieval service
- **Gunicorn**: Production WSGI server

### Frontend
- **React**: Modern UI library
- **Tailwind CSS**: Utility-first CSS framework
- **shadcn/ui**: Beautiful, accessible component library
- **Lucide Icons**: Clean, consistent icon set

## Installation

### Prerequisites
- Python 3.11+
- Node.js 22+ (for frontend development)
- OpenAI API key

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/mikee-ai/bible-study-app.git
cd bible-study-app
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

5. Run the development server:
```bash
python src/main.py
```

The API will be available at `http://localhost:5000`

### Frontend Development

The frontend is already built and included in `src/static/`. To modify the frontend:

1. Navigate to the frontend directory:
```bash
cd ../bible-study-frontend
```

2. Install dependencies:
```bash
pnpm install
```

3. Run development server:
```bash
pnpm run dev
```

4. Build for production:
```bash
pnpm run build
```

5. Copy build to Flask static directory:
```bash
cp -r dist/* ../bible_study_api/src/static/
```

## API Endpoints

### GET /api/verse
Fetch a Bible verse by reference.

**Query Parameters:**
- `reference` (required): Bible reference (e.g., "John 3:16")
- `translation` (optional): Bible translation (default: "kjv")

**Example:**
```bash
curl "http://localhost:5000/api/verse?reference=Romans%208:15"
```

### POST /api/analyze
Analyze scripture through sonship lens.

**Request Body:**
```json
{
  "reference": "Romans 8:15",
  "text": "For ye have not received the spirit of bondage...",
  "translation": "kjv"
}
```

### POST /api/ask
Ask a question about scripture.

**Request Body:**
```json
{
  "reference": "Romans 8:15",
  "text": "For ye have not received the spirit of bondage...",
  "question": "What does Abba mean?"
}
```

### GET /api/study
Get a study guide on a sonship topic.

**Query Parameters:**
- `topic` (required): Topic name (e.g., "adoption", "inheritance")

**Example:**
```bash
curl "http://localhost:5000/api/study?topic=adoption"
```

## Deployment

See [DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md) for detailed instructions on deploying to a VPS.

### Quick Deploy with Gunicorn

```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 wsgi:app
```

### Deploy with Nginx

Configure Nginx as a reverse proxy:

```nginx
location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

## Sonship Theology Framework

The application emphasizes key biblical themes related to sonship:

**Adoption** - Believers are adopted into God's family (Romans 8:15, Galatians 4:5, Ephesians 1:5)

**Inheritance** - Co-heirs with Christ, receiving all the promises (Romans 8:17, Galatians 4:7)

**Intimacy** - Abba, Father relationship - deep personal connection with God (Romans 8:15, Galatians 4:6)

**Identity** - Who we are in Christ as children of God, not what we do

**Freedom** - From law, fear, condemnation, and orphan mindset (Galatians 4:7, Romans 8:1-2)

**Spirit of Adoption** - The Holy Spirit testifies that we are God's children (Romans 8:16)

**Maturity** - Growing from children to mature sons who reflect the Father (Ephesians 4:13-15)

## Key Scripture References

- **Romans 8:14-17** - Led by Spirit, Abba Father, co-heirs
- **Galatians 4:4-7** - Adoption, no longer slaves, heirs
- **Ephesians 1:3-6** - Predestined for adoption, accepted in the Beloved
- **1 John 3:1-2** - Behold what manner of love, we are children of God
- **John 1:12** - Right to become children of God

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is created for ministry purposes to help believers understand their identity in Christ.

## Acknowledgments

- Bible verses provided by [Bible API](https://bible-api.com)
- AI analysis powered by OpenAI
- UI components from [shadcn/ui](https://ui.shadcn.com)

## Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ for God's children**
