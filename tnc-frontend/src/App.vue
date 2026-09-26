<template>
  <div class="container">
    <header>
      <h1>Terms & Conditions Summarizer</h1>
      <p>วิเคราะห์และสรุปเงื่อนไขการให้บริการด้วย AI</p>
    </header>

    <main>
      <!-- ส่วนนำเข้าข้อมูล -->
      <section class="input-section">
        <div class="tabs">
          <button :class="{ active: inputMode === 'text' }" @click="inputMode = 'text'">วางข้อความ</button>
          <button :class="{ active: inputMode === 'file' }" @click="inputMode = 'file'">อัปโหลดไฟล์</button>
        </div>

        <!-- โหมดข้อความ -->
        <div v-if="inputMode === 'text'" class="input-content">
          <textarea v-model="inputText" rows="8" placeholder="วางข้อความ Terms & Conditions หรือ Privacy Policy ที่นี่..."></textarea>
          <button @click="analyzeText" :disabled="loading || !inputText" class="btn-primary">
            {{ loading ? 'กำลังวิเคราะห์...' : 'วิเคราะห์ข้อความ' }}
          </button>
        </div>

        <!-- โหมดไฟล์ -->
        <div v-if="inputMode === 'file'" class="input-content">
          <input type="file" ref="fileInput" @change="handleFileChange" accept=".pdf,.txt" class="file-input" />
          <button @click="analyzeFile" :disabled="loading || !selectedFile" class="btn-primary">
            {{ loading ? 'กำลังวิเคราะห์...' : 'วิเคราะห์ไฟล์' }}
          </button>
        </div>

        <div v-if="error" class="error-msg">{{ error }}</div>
      </section>

      <!-- ส่วนแสดงผลลัพธ์ -->
      <section v-if="result" class="result-section">
        <h2>ผลการวิเคราะห์</h2>
        
        <div class="card">
          <h3>📝 สรุปเนื้อหาสำคัญ</h3>
          <p>{{ result.summary }}</p>
        </div>

        <div class="grid-2">
          <div class="card">
            <h3>🗄️ การเก็บข้อมูลส่วนบุคคล</h3>
            <p>{{ result.data_collection }}</p>
          </div>
          <div class="card">
            <h3>🤝 การแชร์ข้อมูลให้บุคคลที่สาม</h3>
            <p>{{ result.data_sharing }}</p>
          </div>
          <div class="card">
            <h3>💳 เงื่อนไขการชำระเงิน</h3>
            <p>{{ result.payment_terms }}</p>
          </div>
          <div class="card">
            <h3>🚫 ข้อจำกัดของผู้ใช้งาน</h3>
            <p>{{ result.user_restrictions }}</p>
          </div>
        </div>

        <div class="card alert">
          <h3>⚠️ ข้อกำหนดที่อาจมีความเสี่ยง</h3>
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

const inputMode = ref('text')
const inputText = ref('')
const selectedFile = ref(null)
const loading = ref(false)
const result = ref(null)
const error = ref('')

const API_BASE_URL = 'http://127.0.0.1:8000' // URL ของ Backend

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

    const response = await axios.post(`${API_BASE_URL}/api/analyze/text`, formData)
    result.value = response.data.data
  } catch (err) {
    error.value = 'เกิดข้อผิดพลาดในการวิเคราะห์ กรุณาลองใหม่อีกครั้ง'
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

    const response = await axios.post(`${API_BASE_URL}/api/analyze/file`, formData)
    result.value = response.data.data
  } catch (err) {
    error.value = 'เกิดข้อผิดพลาดในการอัปโหลดหรือวิเคราะห์ไฟล์'
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

header {
  text-align: center;
  margin-bottom: 30px;
}

h1 {
  color: #2c3e50;
  margin-bottom: 5px;
}

.input-section {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.tabs {
  margin-bottom: 15px;
  display: flex;
  gap: 10px;
}

.tabs button {
  padding: 8px 16px;
  border: none;
  background: #e9ecef;
  cursor: pointer;
  border-radius: 4px;
}

.tabs button.active {
  background: #42b883;
  color: white;
}

.input-content {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  resize: vertical;
}

.file-input {
  padding: 10px 0;
}

.btn-primary {
  padding: 10px 20px;
  background: #34495e;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.btn-primary:disabled {
  background: #95a5a6;
  cursor: not-allowed;
}

.error-msg {
  color: #e74c3c;
  margin-top: 10px;
}

.result-section h2 {
  text-align: center;
  margin-bottom: 20px;
}

.card {
  background: white;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  margin-bottom: 15px;
}

.card h3 {
  margin-top: 0;
  color: #2c3e50;
  font-size: 1.1em;
}

.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

.card.alert {
  border-left: 5px solid #e74c3c;
  background: #fdf2f1;
}

ul {
  padding-left: 20px;
  margin-bottom: 0;
}
</style>