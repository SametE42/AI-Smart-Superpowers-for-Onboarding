# Security Review

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> წყარო ენა: ინგლისური
> წყარო ფაილი: ai/English/prompts/security-review.md
> განსხვავების შემთხვევაში უპირატესობა აქვს ინგლისურ ფაილს.

ეს გვერდი განმარტავს, როგორ ჯდება `prompts/security-review.md` AI Agent Operating Manual-ში ადამიანებისა და AI agents-ისთვის, რომლებიც repository სამუშაოს გეგმავენ, ამოწმებენ ან იმეორებენ.

## პრაქტიკული ფარგლები

გამოიყენე ეს გვერდი `prompts` თემის ოპერაციულ გზამკვლევად. ის არ ცვლის repository მტკიცებულებებს ან პროექტის ინსტრუქციებს.

## სამუშაო წესები

- ფაილის სახელები, commands, API სახელები და model სახელები უცვლელად შეინახე.
- დაუმოწმებელი დასკვნები მონიშნე `[ASSUMPTION: ...]`, უცნობი ფაქტები `[UNKNOWN]`.
- security, permissions და production-readiness რისკები ადამიანის გადახედვაზე გადაიტანე.

## ფოკუსი

workflow-ში გამოყენებამდე განსაზღვრე ფარგლები, მტკიცებულებები, შემოწმებადი commands და ადამიანის დამტკიცების საზღვრები.


## ხარისხის შემოწმება

- მიზანი ნათელია ახალი contributor-ისთვის.
- ინგლისური წყარო გადამწყვეტია localization კონფლიქტებში.
