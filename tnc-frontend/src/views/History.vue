<template>
  <div class="history-container">
    <div class="page-header">
      <div>
        <h1>Analysis History</h1>
        <p>View your previous document analyses.</p>
      </div>

      <button
        v-if="history.length > 0"
        class="clear-btn"
        @click="clearHistory"
      >
        Clear History
      </button>
    </div>

    <div v-if="history.length === 0" class="empty-state">
      <div class="empty-icon">📄</div>

      <h2>No analysis history</h2>

      <p>
        Your analyzed documents will appear here.
      </p>

      <router-link to="/analyze" class="analyze-btn">
        Analyze a Document
      </router-link>
    </div>

    <div v-else class="history-list">
      <div
        v-for="item in history"
        :key="item.id"
        class="history-card"
      >
        <div class="history-header">
          <div>
            <span class="type-badge">
              {{ item.type === 'file' ? 'File' : 'Text' }}
            </span>

            <span class="language">
              {{ item.language === 'th' ? 'ไทย' : 'English' }}
            </span>
          </div>

          <span class="date">
            {{ formatDate(item.date) }}
          </span>
        </div>

        <h3>Summary</h3>

        <p class="summary">
          {{ item.result.summary }}
        </p>

        <details>
          <summary>View full analysis</summary>

          <div class="details-content">
            <div>
              <h4>🗄️ Data Collection</h4>
              <p>{{ item.result.data_collection }}</p>
            </div>

            <div>
              <h4>🤝 Data Sharing</h4>
              <p>{{ item.result.data_sharing }}</p>
            </div>

            <div>
              <h4>💳 Payment Terms</h4>
              <p>{{ item.result.payment_terms }}</p>
            </div>

            <div>
              <h4>🚫 User Restrictions</h4>
              <p>{{ item.result.user_restrictions }}</p>
            </div>

            <div class="risk-section">
              <h4>⚠️ Potentially Risky Clauses</h4>

              <ul>
                <li
                  v-for="(risk, index) in item.result.risky_clauses"
                  :key="index"
                >
                  {{ risk }}
                </li>
              </ul>
            </div>
          </div>
        </details>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const history = ref([])

const loadHistory = () => {
  history.value = JSON.parse(
    localStorage.getItem('analysisHistory') || '[]'
  )
}

const clearHistory = () => {
  const confirmed = window.confirm(
    'Are you sure you want to clear all analysis history?'
  )

  if (!confirmed) {
    return
  }

  localStorage.removeItem('analysisHistory')
  history.value = []
}

const formatDate = (date) => {
  return new Date(date).toLocaleString()
}

onMounted(() => {
  loadHistory()
})
</script>

<style scoped>
.history-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 20px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.page-header h1 {
  margin: 0 0 8px;
  color: #2c3e50;
}

.page-header p {
  margin: 0;
  color: #6c757d;
}

.clear-btn {
  padding: 9px 16px;
  background: white;
  color: #e74c3c;
  border: 1px solid #e74c3c;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}

.clear-btn:hover {
  background: #fdf2f1;
}

.empty-state {
  background: white;
  border-radius: 10px;
  padding: 60px 20px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.empty-icon {
  font-size: 50px;
  margin-bottom: 15px;
}

.empty-state h2 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.empty-state p {
  color: #6c757d;
  margin-bottom: 25px;
}

.analyze-btn {
  display: inline-block;
  padding: 10px 20px;
  background: #42b883;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 600;
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.history-card {
  background: white;
  padding: 22px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.history-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.type-badge {
  display: inline-block;
  padding: 4px 9px;
  background: #e8f5ef;
  color: #2d8a61;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.language {
  margin-left: 8px;
  color: #6c757d;
  font-size: 13px;
}

.date {
  color: #6c757d;
  font-size: 13px;
}

.history-card h3 {
  margin-bottom: 8px;
  color: #2c3e50;
}

.summary {
  color: #555;
  line-height: 1.6;
}

details {
  margin-top: 15px;
  border-top: 1px solid #eee;
  padding-top: 15px;
}

summary {
  cursor: pointer;
  font-weight: 600;
  color: #34495e;
}

.details-content {
  margin-top: 20px;
}

.details-content > div {
  margin-bottom: 20px;
}

.details-content h4 {
  margin-bottom: 8px;
  color: #2c3e50;
}

.details-content p {
  line-height: 1.6;
  color: #555;
}

.risk-section {
  background: #fdf2f1;
  border-left: 4px solid #e74c3c;
  padding: 15px;
}

.risk-section ul {
  padding-left: 20px;
}

.risk-section li {
  margin-bottom: 8px;
  line-height: 1.5;
}

@media (max-width: 600px) {
  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .history-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
}
</style>