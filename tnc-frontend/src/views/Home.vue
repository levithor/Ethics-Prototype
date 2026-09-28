<template>
  <div class="home">
    <section class="hero">
      <div class="hero-content">
        <h1>Understand Terms & Conditions with AI</h1>

        <p>
          Quickly analyze Terms & Conditions and Privacy Policies
          and understand the important information without reading
          complicated legal language.
        </p>

        <router-link to="/analyze" class="btn-primary">
          Start Analyzing
        </router-link>
      </div>
    </section>

    <section class="features">
      <h2>What can you analyze?</h2>

      <div class="feature-grid">
        <div class="feature-card">
          <div class="icon">📝</div>
          <h3>Key Summary</h3>
          <p>
            Get a simple summary of the most important information
            in the document.
          </p>
        </div>

        <div class="feature-card">
          <div class="icon">🗄️</div>
          <h3>Data Collection</h3>
          <p>
            Understand what personal information is collected and
            how it is used.
          </p>
        </div>

        <div class="feature-card">
          <div class="icon">🤝</div>
          <h3>Data Sharing</h3>
          <p>
            Find out whether your information may be shared with
            third parties.
          </p>
        </div>

        <div class="feature-card">
          <div class="icon">⚠️</div>
          <h3>Potential Risks</h3>
          <p>
            Identify clauses that may require extra attention,
            such as automatic renewal or account termination.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home {
  min-height: calc(100vh - 70px);
}

.hero {
  padding: 100px 20px;
  text-align: center;
  background: #f1f8f5;
}

.hero-content {
  max-width: 700px;
  margin: 0 auto;
}

.hero h1 {
  font-size: 44px;
  color: #2c3e50;
  margin-bottom: 20px;
}

.hero p {
  font-size: 18px;
  line-height: 1.7;
  color: #667085;
  margin-bottom: 35px;
}

.btn-primary {
  display: inline-block;
  padding: 12px 24px;
  background: #42b883;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 600;
  transition: 0.2s;
}

.btn-primary:hover {
  background: #369f6e;
}

.features {
  max-width: 1000px;
  margin: 0 auto;
  padding: 60px 20px;
}

.features h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 35px;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.feature-card {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.feature-card .icon {
  font-size: 30px;
  margin-bottom: 10px;
}

.feature-card h3 {
  margin: 0 0 10px;
  color: #2c3e50;
}

.feature-card p {
  color: #667085;
  line-height: 1.6;
  margin-bottom: 0;
}

@media (max-width: 700px) {
  .hero {
    padding: 70px 20px;
  }

  .hero h1 {
    font-size: 34px;
  }

  .feature-grid {
    grid-template-columns: 1fr;
  }
}
</style>