# Rag

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> উৎস ভাষা: ইংরেজি
> উৎস ফাইল: ai/English/context-engineering/rag.md
> পার্থক্য থাকলে ইংরেজি ফাইল প্রাধান্য পাবে।

এই পৃষ্ঠা ব্যাখ্যা করে `context-engineering/rag.md` কীভাবে AI Agent Operating Manual-এর মধ্যে ব্যবহৃত হয়। এটি repository কাজ পরিকল্পনা, যাচাই বা পুনরাবৃত্তি করতে হয় এমন মানুষ ও AI agents-এর জন্য লেখা।

## ব্যবহারিক পরিসর

এই পৃষ্ঠাকে `context-engineering` বিষয়ের কার্যকরী নির্দেশিকা হিসেবে ব্যবহার করুন। এটি repository প্রমাণ বা প্রকল্প-নির্দিষ্ট নির্দেশের বিকল্প নয়।

## কাজের নির্দেশিকা

- repository প্রমাণকে প্রধান কর্তৃত্ব হিসেবে ধরুন।
- ফাইলের নাম, commands, API নাম এবং model নাম অপরিবর্তিত রাখুন।
- যাচাইহীন সিদ্ধান্ত `[ASSUMPTION: ...]` এবং অজানা তথ্য `[UNKNOWN]` দিয়ে চিহ্নিত করুন।
- tool-নির্দিষ্ট আচরণকে সেই tool বা runtime-এর সঙ্গে যুক্ত করুন যা সত্যিই তা নিয়ন্ত্রণ করে।
- নিরাপত্তা, permissions এবং production-readiness ঝুঁকি মানব পর্যালোচনায় পাঠান।

## ফোকাস

workflow-তে এই পৃষ্ঠা ব্যবহারের আগে পরিসর, প্রয়োজনীয় প্রমাণ, যাচাইযোগ্য commands এবং মানব অনুমোদনের সীমা নির্ধারণ করুন।


## গুণমান পরীক্ষা

- উদ্দেশ্য নতুন contributor-এর কাছে পরিষ্কার।
- নির্দেশিকা AI agents এবং মানব maintainers উভয়ের জন্য সহায়ক।
- model-নির্দিষ্ট commands বানানো হয় না।
- নিরাপত্তা ও মানব অনুমোদনের সীমা দৃশ্যমান থাকে।
- localization সংঘাতে ইংরেজি উৎস সিদ্ধান্তমূলক থাকে।
