<template>
  <div class="container">
    <header>
      <div class="header-top">
        <h1>{{ t[locale].title }}</h1>
        <button class="lang-btn" @click="toggleLanguage">
          <!-- แสดงธงและข้อความตามภาษาปัจจุบัน -->
          <img v-if="locale === 'th'" src="/UKUS.png" alt="English" class="flag-icon" />
          <span v-if="locale === 'th'">EN</span>

          <img v-if="locale === 'en'" src="/Thai.png" alt="Thai" class="flag-icon" />
          <span v-if="locale === 'en'">TH</span>
        </button>
      </div>
      <p>{{ t[locale].subtitle }}</p>
    </header>

    <main>
      <!-- ส่วนนำเข้าข้อมูล -->
      <section class="input-section">
        <div class="tabs">
          <button :class="{ active: inputMode === 'text' }" @click="inputMode = 'text'">
            {{ t[locale].pasteText }}
          </button>
          <button :class="{ active: inputMode === 'file' }" @click="inputMode = 'file'">
            {{ t[locale].uploadFile }}
          </button>
        </div>

        <!-- โหมดข้อความ -->
        <div v-if="inputMode === 'text'" class="input-content">
          <textarea v-model="inputText" rows="8" :placeholder="t[locale].placeholder"></textarea>
          <button @click="analyzeText" :disabled="loading || !inputText" class="btn-primary">
            {{ loading ? t[locale].analyzing : t[locale].analyzeTextBtn }}
          </button>
        </div>

        <!-- โหมดไฟล์ -->
        <div v-if="inputMode === 'file'" class="input-content">
          <input type="file" ref="fileInput" @change="handleFileChange" accept=".pdf,.txt" class="file-input" />
          <button @click="analyzeFile" :disabled="loading || !selectedFile" class="btn-primary">
            {{ loading ? t[locale].analyzing : t[locale].analyzeFileBtn }}
          </button>
        </div>

        <div v-if="error" class="error-msg">{{ error }}</div>
      </section>

      <!-- ส่วนแสดงผลลัพธ์ -->
      <section v-if="result" class="result-section">
        <h2>{{ t[locale].resultTitle }}</h2>
        
        <div class="card">
          <h3>{{ t[locale].summary }}</h3>
          <p>{{ result.summary }}</p>
        </div>

        <div class="grid-2">
          <div class="card">
            <h3>{{ t[locale].dataCollection }}</h3>
            <p>{{ result.data_collection }}</p>
          </div>
          <div class="card">
            <h3>{{ t[locale].dataSharing }}</h3>
            <p>{{ result.data_sharing }}</p>
          </div>
          <div class="card">
            <h3>{{ t[locale].paymentTerms }}</h3>
            <p>{{ result.payment_terms }}</p>
          </div>
          <div class="card">
            <h3>{{ t[locale].userRestrictions }}</h3>
            <p>{{ result.user_restrictions }}</p>
          </div>
        </div>

        <div class="card alert">
          <h3>{{ t[locale].riskyClauses }}</h3>
          <ul>
            <li v-for="(risk, index) in result.risky_clauses" :key="index">{{ risk }}</li>
          </ul>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const locale = ref('th') // ค่าเริ่มต้นเป็นภาษาไทย
const inputMode = ref('text')
const inputText = ref('')
const selectedFile = ref(null)
const loading = ref(false)
const result = ref(null)
const error = ref('')

// ข้อความแยกตามภาษา
const t = {
  th: {
    title: 'Terms & Conditions Summarizer',
    subtitle: 'วิเคราะห์และสรุปเงื่อนไขการให้บริการด้วย AI',
    pasteText: 'วางข้อความ',
    uploadFile: 'อัปโหลดไฟล์',
    placeholder: 'วางข้อความ Terms & Conditions หรือ Privacy Policy ที่นี่...',
    analyzeTextBtn: 'วิเคราะห์ข้อความ',
    analyzeFileBtn: 'วิเคราะห์ไฟล์',
    analyzing: 'กำลังวิเคราะห์...',
    resultTitle: 'ผลการวิเคราะห์',
    summary: '📝 สรุปเนื้อหาสำคัญ',
    dataCollection: '🗄️ การเก็บข้อมูลส่วนบุคคล',
    dataSharing: '🤝 การแชร์ข้อมูลให้บุคคลที่สาม',
    paymentTerms: '💳 เงื่อนไขการชำระเงิน',
    userRestrictions: '🚫 ข้อจำกัดของผู้ใช้งาน',
    riskyClauses: '⚠️ ข้อกำหนดที่อาจมีความเสี่ยง',
    errorText: 'เกิดข้อผิดพลาดในการวิเคราะห์ กรุณาลองใหม่อีกครั้ง'
  },
  en: {
    title: 'Terms & Conditions Summarizer',
    subtitle: 'Analyze and summarize terms of service with AI',
    pasteText: 'Paste Text',
    uploadFile: 'Upload File',
    placeholder: 'Paste Terms & Conditions or Privacy Policy here...',
    analyzeTextBtn: 'Analyze Text',
    analyzeFileBtn: 'Analyze File',
    analyzing: 'Analyzing...',
    resultTitle: 'Analysis Result',
    summary: '📝 Key Summary',
    dataCollection: '🗄️ Data Collection',
    dataSharing: '🤝 Data Sharing',
    paymentTerms: '💳 Payment Terms',
    userRestrictions: '🚫 User Restrictions',
    riskyClauses: '⚠️ Potentially Risky Clauses',
    errorText: 'An error occurred during analysis. Please try again.'
  }
}

const toggleLanguage = () => {
  locale.value = locale.value === 'th' ? 'en' : 'th'
}

const API_BASE_URL = 'http://127.0.0.1:8000' // อย่าลืมเปลี่ยนเป็น URL ของ Render เมื่อเอาขึ้นออนไลน์

const handleFileChange = (event) => {
  selectedFile.value = event.target.files[0]
}

const analyzeText = async () => {
  loading.value = true
  error.value = ''
  result.value = null

  try {
    const formData = new FormData()
    formData.append('text', inputText.value)
    // หากต้องการให้ AI ตอบเป็นภาษาอังกฤษด้วย สามารถส่ง locale ไปบอก Backend ได้
    formData.append('language', locale.value) 

    const response = await axios.post(`${API_BASE_URL}/api/analyze/text`, formData)
    result.value = response.data.data
  } catch (err) {
    error.value = t[locale.value].errorText
    console.error(err)
  } finally {
    loading.value = false
  }
}

const analyzeFile = async () => {
  loading.value = true
  error.value = ''
  result.value = null

  try {
    const formData = new FormData()
    formData.append('file', selectedFile.value)
    formData.append('language', locale.value)

    const response = await axios.post(`${API_BASE_URL}/api/analyze/file`, formData)
    result.value = response.data.data
  } catch (err) {
    error.value = t[locale.value].errorText
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

.header-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.lang-btn {
  background: #f1f3f5;
  border: 1px solid #ced4da;
  padding: 5px 12px;
  border-radius: 20px;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.2s;
  /* เพิ่มการจัดเรียงเพื่อให้ธงกับตัวหนังสืออยู่ตรงกัน */
  display: flex;
  align-items: center;
  gap: 8px;
}

.flag-icon {
  width: 20px;
  height: 15px; /* ปรับความสูงตามสัดส่วนของรูปภาพคุณ */
  object-fit: cover;
  border-radius: 2px;
}

.lang-btn:hover {
  background: #e9ecef;
}

header p {
  margin-top: 5px;
  color: #6c757d;
}

/* (สไตล์อื่นๆ คงเดิมจากเวอร์ชันก่อนหน้า) */
.input-section { background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
.tabs { margin-bottom: 15px; display: flex; gap: 10px; }
.tabs button { padding: 8px 16px; border: none; background: #e9ecef; cursor: pointer; border-radius: 4px; }
.tabs button.active { background: #42b883; color: white; }
.input-content { display: flex; flex-direction: column; gap: 15px; }
textarea { width: 100%; padding: 10px; border: 1px solid #ced4da; border-radius: 4px; resize: vertical; }
.file-input { padding: 10px 0; }
.btn-primary { padding: 10px 20px; background: #34495e; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
.btn-primary:disabled { background: #95a5a6; cursor: not-allowed; }
.error-msg { color: #e74c3c; margin-top: 10px; }
.result-section h2 { text-align: center; margin-bottom: 20px; }
.card { background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 15px; }
.card h3 { margin-top: 0; color: #2c3e50; font-size: 1.1em; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
.card.alert { border-left: 5px solid #e74c3c; background: #fdf2f1; }
ul { padding-left: 20px; margin-bottom: 0; }
</style>