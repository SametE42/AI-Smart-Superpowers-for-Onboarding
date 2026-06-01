# Model Comparison

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> زبان مبدأ: انگلیسی
> فایل مبدأ: ai/English/workflows/model-comparison.md
> در صورت اختلاف، فایل انگلیسی مرجع اصلی است.

این صفحه توضیح می‌دهد که `workflows/model-comparison.md` چگونه در AI Agent Operating Manual قرار می‌گیرد. برای انسان‌ها و AI agents نوشته شده که باید کار repository را برنامه‌ریزی، راستی‌آزمایی یا تکرار کنند.

## دامنه عملی

از این صفحه به عنوان راهنمای عملیاتی برای موضوع `workflows` استفاده کنید. جایگزین شواهد repository یا دستورهای اختصاصی پروژه نیست.

## راهنمای کار

- شواهد repository را مرجع اصلی بدانید.
- نام فایل‌ها، commands، نام‌های API و نام مدل‌ها را دقیقاً حفظ کنید.
- نتیجه‌های تأییدنشده را با `[ASSUMPTION: ...]` و واقعیت‌های ناشناخته را با `[UNKNOWN]` علامت بزنید.
- رفتار ویژه ابزار را به همان tool یا runtime که واقعاً مالک آن است وصل کنید.
- ریسک‌های security، permissions و production-readiness را به بازبینی انسانی ارجاع دهید.

## تمرکز

پیش از استفاده از این صفحه در workflow، دامنه، شواهد لازم، commands قابل راستی‌آزمایی و مرزهای تأیید انسانی را تعریف کنید.

## کنترل کیفیت

- هدف برای contributor جدید روشن است.
- راهنما برای AI agents و maintainers انسانی مفید است.
- commands اختصاصی مدل‌ها ساخته نمی‌شوند.
- مرزهای security و تأیید انسانی قابل مشاهده می‌مانند.
- در تعارض‌های localization، منبع انگلیسی تعیین‌کننده است.
