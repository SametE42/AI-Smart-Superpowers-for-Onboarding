# Planner Executor

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> Kaynak dil: İngilizce
> Kaynak dosya: ai/English/agents/planner-executor.md
> Tutarsızlık olduğunda İngilizce dosya esas alınır.

Bu sayfa `agents/planner-executor.md` dosyasının AI Agent Operating Manual içinde nasıl kullanıldığını açıklar. Depo çalışmasını planlaması, doğrulaması veya tekrarlaması gereken insanlar ve yapay zeka ajanları için yazılmıştır.

## Pratik kapsam

Bu sayfayı `agents` konusu için operasyonel yönlendirme olarak kullan. Depo kanıtlarının veya projeye özel talimatların yerine geçmez.

## Çalışma yönergeleri

- Depo kanıtlarını birincil otorite olarak kabul et.
- Dosya adlarını, komutları, API adlarını ve model adlarını aynen koru.
- Doğrulanmamış sonuçları `[ASSUMPTION: ...]`, bilinmeyen gerçekleri `[UNKNOWN]` olarak işaretle.
- Araca özgü davranışı gerçekten o davranışın sahibi olan araç veya runtime ile ilişkilendir.
- Güvenlik, izin ve üretime hazırlık risklerini insan incelemesine yükselt.

## Odak

Bu sayfayı bir workflow içinde kullanmadan önce kapsamı, gerekli kanıtları, doğrulanabilir komutları ve insan onayı sınırlarını tanımla.


## Kalite kontrolü

- Amaç yeni katkı sağlayanlar için açıktır.
- Yönergeler hem yapay zeka ajanlarına hem de insan bakımcılara yardımcı olur.
- Modele özgü komutlar uydurulmaz.
- Güvenlik ve insan onayı sınırları görünür kalır.
- Yerelleştirme çakışmalarında İngilizce kaynak otorite olmaya devam eder.
