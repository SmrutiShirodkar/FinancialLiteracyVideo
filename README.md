# AI-Powered Financial Literacy Video Generator  

## **Overview**  
Overview

This project is the initial step in merging AI with financial education. It automates the creation of short, engaging videos summarizing financial concepts and news, making learning accessible and interactive for everyone. By leveraging machine learning models, this tool converts textual content into visually appealing video summaries, paving the way for a more inclusive, gamified approach to financial literacy.
   
---

## **Features**  
1. **Content Summarization**:  
   Summarizes lengthy text content into concise, digestible snippets.  

2. **Keyword Extraction**:  
   Identifies essential keywords from text to guide image selection.  

3. **Visual Content Creation**:  
   Downloads relevant images and overlays summarized text for context.  

4. **Video Generation**:  
   Compiles processed images into a cohesive short-format video.  

---

## **Project Structure Rough**  


FinancialLiteracyVideo/
├── data/
│   ├── input.txt           # Input text for summarization
│   ├── input.pdf           # (New) PDF file for scraping
├── images/
│   ├── downloaded/         # Images fetched using keywords
├── output/
│   ├── video.mp4           # Final generated video
├── scripts/
│   ├── pdf_scraper.py      # (New) Script to extract text from PDFs
│   ├── summarizer.py       # Script for summarization
│   ├── keyword_extractor.py # Script for keyword extraction
│   ├── image_downloader.py  # Script to download images
│   ├── overlay_text.py     # Script to overlay text on images
│   ├── video_creator.py    # Main script to execute the program
├── requirements.txt        # Dependencies
├── README.md               # Documentation

---

#### **How It Works**  

1. **Provide Input**:  
   Based on an article or text content sourced in the `data/input.txt` file.  

2. **Run the Script**:  
   Execute the `video_creator.py` script to process the input text and create a video.  

3. **Output**:  
   The resulting video is saved in the `output/video.mp4` folder, ready for review or sharing.  

---

#### **Technologies Used**  
- **Python Libraries**:  
  - `transformers`: For text summarization.  
  - `KeyBERT`: For keyword extraction.  
  - `google_images_download`: For fetching relevant images.  
  - `cv2` (OpenCV): For image processing and text overlay.  
  - `skvideo`: For video creation.  

- **Machine Learning**: Pre-trained models for text analysis and summarization.  

---

#### **Future Scope**  

This project represents the foundational phase of integrating AI and finance education. Future plans include:  
- **Advanced Personalization**:  
  User-specific financial learning paths and adaptive content.  

- **Interactive Features**:  
  Gamified simulations and quizzes within videos to boost engagement.  

- **Multilingual Support**:  
  Multiple languages for global accessibility.  

- **Ethical AI Use**:  
  Fairness and inclusivity in content generation.  

---

#### **Acknowledgments**  
This project builds upon foundational ideas in using AI for personalized learning. It marks the first step toward democratizing financial education through innovative technologies.  






