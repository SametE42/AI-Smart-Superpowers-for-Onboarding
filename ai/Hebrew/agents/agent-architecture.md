# Agent Architecture

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> שפת מקור: אנגלית
> קובץ מקור: ai/English/agents/agent-architecture.md
> במקרה של סתירה, הקובץ באנגלית הוא הקובע.

דף זה מסביר כיצד `agents/agent-architecture.md` משתלב ב-AI Agent Operating Manual. הוא מיועד לאנשים ול-AI agents שצריכים לתכנן, לאמת או לחזור על עבודה ב-repository.

## היקף מעשי

השתמש בדף זה כהנחיה תפעולית לנושא `agents`. הוא אינו מחליף ראיות מה-repository או הוראות ייחודיות לפרויקט.

## הנחיות עבודה

- התייחס לראיות מה-repository כסמכות העיקרית.
- שמור בדיוק על שמות קבצים, commands, שמות API ושמות מודלים.
- סמן מסקנות לא מאומתות עם `[ASSUMPTION: ...]` ועובדות לא ידועות עם `[UNKNOWN]`.
- קשר התנהגות ייחודית לכלי אל ה-tool או runtime שבאמת מחזיק בה.
- העבר סיכוני security, permissions ו-production-readiness לביקורת אנושית.

## מיקוד

לפני שימוש בדף זה ב-workflow, הגדר היקף, ראיות נדרשות, commands ניתנים לאימות וגבולות אישור אנושי.


## בדיקת איכות

- המטרה ברורה ל-contributor חדש.
- ההנחיה מועילה גם ל-AI agents וגם ל-maintainers אנושיים.
- לא ממציאים commands ייחודיים למודלים.
- גבולות security ואישור אנושי נשארים גלויים.
- המקור האנגלי נשאר מכריע בסכסוכי localization.
