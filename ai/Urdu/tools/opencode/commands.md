# Commands

<!-- localization-status: localized-mirror; review-status: tracked-in-language-support -->

> Language status: localized mirror of the English reference. Review status is tracked in the language support metadata.
> ماخذ زبان: انگریزی
> ماخذ فائل: ai/English/tools/opencode/commands.md
> اختلاف کی صورت میں انگریزی فائل کو ترجیح حاصل ہوگی۔

یہ صفحہ بتاتا ہے کہ `tools/opencode/commands.md` AI Agent Operating Manual میں کیسے استعمال ہوتا ہے۔ یہ ان انسانوں اور AI agents کے لیے ہے جنہیں repository کام کی منصوبہ بندی، تصدیق یا تکرار کرنی ہوتی ہے۔

## عملی دائرہ

اس صفحے کو `tools` موضوع کے لیے عملی رہنما کے طور پر استعمال کریں۔ یہ repository شواہد یا منصوبے کی مخصوص ہدایات کا بدل نہیں۔

## کام کی ہدایات

- repository شواہد کو بنیادی اتھارٹی سمجھیں۔
- فائل نام، commands، API نام اور model نام بالکل برقرار رکھیں۔
- غیر تصدیق شدہ نتائج کو `[ASSUMPTION: ...]` اور نامعلوم حقائق کو `[UNKNOWN]` سے نشان زد کریں۔
- tool مخصوص رویے کو اسی tool یا runtime سے جوڑیں جو واقعی اس کا مالک ہے۔
- security، permissions اور production-readiness خطرات کو انسانی جائزے تک بڑھائیں۔

## توجہ

اس صفحے کو workflow میں استعمال کرنے سے پہلے دائرہ، مطلوبہ شواہد، قابل تصدیق commands اور انسانی منظوری کی حدود طے کریں۔


## معیار کی جانچ

- مقصد نئے contributor کے لیے واضح ہے۔
- رہنمائی AI agents اور انسانی maintainers دونوں کے لیے مفید ہے۔
- model مخصوص commands ایجاد نہیں کیے جاتے۔
- security اور انسانی منظوری کی حدود واضح رہتی ہیں۔
- localization تنازعات میں انگریزی ماخذ فیصلہ کن رہتا ہے۔
