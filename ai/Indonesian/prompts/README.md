# Prompts

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> Bahasa sumber: Inggris
> File sumber: ai/English/prompts/README.md
> Jika ada perbedaan, file Inggris menjadi acuan.

Halaman ini menjelaskan bagaimana `prompts/README.md` masuk ke AI Agent Operating Manual. Ditulis untuk manusia dan AI agents yang perlu merencanakan, memverifikasi, atau mengulang pekerjaan repository.

## Cakupan praktis

Gunakan halaman ini sebagai panduan operasional untuk tema `prompts`. Ini tidak menggantikan bukti repository atau instruksi khusus proyek.

## Panduan kerja

- Perlakukan bukti repository sebagai otoritas utama.
- Pertahankan nama file, commands, nama API, dan nama model secara persis.
- Tandai kesimpulan yang belum diverifikasi dengan `[ASSUMPTION: ...]` dan fakta yang tidak diketahui dengan `[UNKNOWN]`.
- Hubungkan perilaku khusus tool ke tool atau runtime yang benar-benar memilikinya.
- Eskalasi risiko security, permissions, dan production-readiness ke tinjauan manusia.

## Fokus

Sebelum memakai halaman ini dalam workflow, tetapkan cakupan, bukti yang diperlukan, commands yang dapat diverifikasi, dan batas persetujuan manusia.

## Manual Pages

- [Accuracy Clause](accuracy-clause.md)
- [Code Review](code-review.md)
- [Documentation Update](documentation-update.md)
- [Magical Prompt Improver](magical-prompt-improver.md)
- [Master Prompt](master-prompt.md)
- [Prompt Refinement](prompt-refinement.md)
- [Prompt Structure](prompt-structure.md)
- [Security Review](security-review.md)
- [Translation](translation.md)


## Pemeriksaan kualitas

- Tujuan jelas bagi contributor baru.
- Panduan berguna bagi AI agents dan maintainer manusia.
- Tidak ada commands khusus model yang dikarang.
- Batas security dan persetujuan manusia tetap terlihat.
- Sumber Inggris tetap menentukan saat konflik localization.
