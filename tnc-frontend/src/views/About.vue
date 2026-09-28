```vue
<template>
  <div class="about-container">
    <!-- Intro -->
    <section class="intro-section">
      <h1>About T&C Lens</h1>

      <p class="intro-text">
        T&C Lens is an educational tool that analyzes Terms & Conditions
        and Privacy Policies and converts complex legal material into
        easier-to-understand information.
      </p>
    </section>

    <!-- What it does / does not do -->
    <section class="comparison-section">
      <div class="column">
        <h2>What it does</h2>

        <ul>
          <li>Analyzes Terms & Conditions and Privacy Policies</li>
          <li>
            Converts complex legal language into plain-language summaries
          </li>
          <li>
            Identifies data collection, sharing, and tracking practices
          </li>
          <li>
            Highlights subscriptions, payments, and automatic renewals
          </li>
          <li>
            Detects potentially concerning clauses and assigns risk levels
          </li>
          <li>
            Lets you compare AI explanations with the original source text
          </li>
        </ul>
      </div>

      <div class="column">
        <h2>What it does not do</h2>

        <ul>
          <li>Replace the original document — always review the source</li>
          <li>Provide legal advice or legal opinions</li>
          <li>
            Determine whether a contract is legally valid or enforceable
          </li>
          <li>
            Guarantee accuracy — AI output may be incomplete or inaccurate
          </li>
        </ul>
      </div>
    </section>

    <!-- Why it exists -->
    <section class="why-section">
      <h2>Why it exists</h2>

      <p class="why-text">
        Most people accept digital agreements without understanding what
        they're agreeing to. Complex legal language prevents users from
        grasping privacy implications, data collection, sharing practices,
        and other obligations before clicking "Accept." T&C Lens exists
        to make these points easier to understand — not to make the
        decision for you.
      </p>
    </section>
  </div>
</template>

<style scoped>
.about-container {
  max-width: 850px;
  margin: 0 auto;
  padding: 45px 20px;
  color: #333;
}

/* Intro */
.intro-section {
  margin-bottom: 42px;
}

.intro-section h1 {
  margin: 0 0 12px;
  color: #2c3e50;
  font-size: 38px;
  line-height: 1.2;
}

.intro-text {
  margin-top: 1rem;
  font-size: 1.25rem;
  line-height: 1.75;
  color: #555;
}

/* What it does / does not do */
.comparison-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 55px;
  margin-bottom: 42px;
}

.column h2,
.why-section h2 {
  margin: 0 0 14px;
  color: #2c3e50;
  font-size: 24px;
}

.column ul {
  margin: 0;
  padding-left: 20px;
}

.column li {
  margin-bottom: 9px;
  line-height: 1.5;
  color: #555;
}

/* Why it exists */
.why-section {
  margin-bottom: 20px;
}

.why-text {
  margin-top: 1rem;
  font-size: 1.25rem;
  line-height: 1.75;
  color: #555;
}

@media (max-width: 700px) {
  .about-container {
    padding: 35px 20px;
  }

  .intro-section h1 {
    font-size: 32px;
  }

  .intro-text,
  .why-text {
    font-size: 1.1rem;
  }

  .comparison-section {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}
</style>