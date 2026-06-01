# Optimization Overview

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> ภาษาต้นฉบับ: อังกฤษ
> ไฟล์ต้นฉบับ: ai/English/optimization/optimization-overview.md
> หากมีความแตกต่าง ให้ยึดไฟล์ภาษาอังกฤษเป็นหลัก

หน้านี้อธิบายว่า `optimization/optimization-overview.md` อยู่ใน AI Agent Operating Manual อย่างไร เขียนไว้สำหรับมนุษย์และ AI agents ที่ต้องวางแผน ตรวจสอบ หรือทำซ้ำงานใน repository

## ขอบเขตเชิงปฏิบัติ

ใช้หน้านี้เป็นแนวทางปฏิบัติสำหรับหัวข้อ `optimization` ไม่ใช่สิ่งทดแทนหลักฐานใน repository หรือคำสั่งเฉพาะของโครงการ

## แนวทางการทำงาน

- ถือว่าหลักฐานใน repository เป็นแหล่งอ้างอิงหลัก
- รักษาชื่อไฟล์ commands ชื่อ API และชื่อ model ให้ตรงเดิม
- ทำเครื่องหมายข้อสรุปที่ยังไม่ยืนยันด้วย `[ASSUMPTION: ...]` และข้อเท็จจริงที่ไม่ทราบด้วย `[UNKNOWN]`
- เชื่อมพฤติกรรมเฉพาะของ tool กับ tool หรือ runtime ที่เป็นเจ้าของจริง
- ส่งต่อความเสี่ยงด้าน security, permissions และ production-readiness ให้มนุษย์ตรวจทาน

## จุดเน้น

ก่อนใช้หน้านี้ใน workflow ให้กำหนดขอบเขต หลักฐานที่ต้องใช้ commands ที่ตรวจสอบได้ และขอบเขตการอนุมัติโดยมนุษย์

## การตรวจคุณภาพ

- เป้าหมายชัดเจนสำหรับ contributor ใหม่
- แนวทางช่วยทั้ง AI agents และ maintainer ที่เป็นมนุษย์
- ไม่แต่ง commands เฉพาะ model ขึ้นมาเอง
- ขอบเขต security และการอนุมัติโดยมนุษย์ยังมองเห็นได้
- ต้นฉบับภาษาอังกฤษยังเป็นตัวตัดสินเมื่อเกิดข้อขัดแย้งด้าน localization
