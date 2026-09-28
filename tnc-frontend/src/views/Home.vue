<template>
  <div class="home">
    <!-- Hero -->
    <section class="hero">
      <div class="hero-content">
        <h1>Understand what you're agreeing to.</h1>

        <p>
          Turn complicated Terms & Conditions and Privacy Policies into clear,
          understandable information before you accept.
        </p>

        <div class="hero-buttons">
          <router-link to="/analyze" class="btn-primary">
            Analyze a document
          </router-link>

          <router-link to="/about" class="btn-secondary">
            Learn more
          </router-link>
        </div>
      </div>
    </section>

    <!-- How we will help -->
    <section class="analyze-section">
      <div class="analyze-wrapper">

        <!-- Section heading -->
        <div class="section-heading">
          <h2>How we will help</h2>
        </div>

        <!-- Two-column feature area -->
        <div class="analyze-content">

          <!-- Left side -->
          <div class="feature-navigation">
            <div class="feature-list">
              <button
                v-for="(feature, index) in features"
                :key="feature.number"
                class="feature-tab"
                :class="{ active: activeFeature === index }"
                @mouseenter="activeFeature = index"
                @focus="activeFeature = index"
                @click="activeFeature = index"
              >
                <span class="feature-number">
                  {{ feature.number }}
                </span>

                <span class="feature-title">
                  {{ feature.title }}
                </span>
              </button>
            </div>
          </div>

          <!-- Right side -->
          <div class="feature-detail">
            <Transition name="feature-fade" mode="out-in">
              <div :key="activeFeature">
                <div class="detail-number">
                  {{ features[activeFeature].number }}
                </div>

                <h3>
                  {{ features[activeFeature].insight }}
                </h3>

                <p>
                  {{ features[activeFeature].description }}
                </p>
              </div>
            </Transition>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const activeFeature = ref(0)

const features = [
  {
    number: '01',
    title: 'Summarize lengthy agreements',
    insight: 'Plain-language overview',
    description:
      'Get the main points without reading every page of legal text.'
  },
  {
    number: '02',
    title: 'Identify privacy & data practices',
    insight: 'Know what happens to your data',
    description:
      'See what information is collected, how it is used, and whether it is shared with others.'
  },
  {
    number: '03',
    title: 'Detect concerning clauses',
    insight: 'Know what to look out for',
    description:
      'Find terms such as automatic renewal, arbitration, broad licenses, and liability limitations.'
  },
  {
    number: '04',
    title: 'Understand faster',
    insight: 'See the explanation in context',
    description:
      'Connect each AI explanation back to the original section of the document.'
  }
]

const currentSection = ref(0)
const isScrolling = ref(false)

const easeInOutCubic = (t) => {
  return t < 0.5
    ? 4 * t * t * t
    : 1 - Math.pow(-2 * t + 2, 3) / 2
}

const animateScroll = (targetY, duration = 900) => {
  const startY = window.scrollY
  const distance = targetY - startY
  const startTime = performance.now()

  const animate = (currentTime) => {
    const elapsed = currentTime - startTime
    const progress = Math.min(elapsed / duration, 1)

    const easedProgress = easeInOutCubic(progress)

    window.scrollTo(
      0,
      startY + distance * easedProgress
    )

    if (progress < 1) {
      requestAnimationFrame(animate)
    } else {
      isScrolling.value = false
    }
  }

  requestAnimationFrame(animate)
}

const scrollToSection = (index) => {
  const sections = document.querySelectorAll('.home > section')

  if (index < 0 || index >= sections.length) return

  currentSection.value = index
  isScrolling.value = true

  const targetY =
    sections[index].getBoundingClientRect().top + window.scrollY

  animateScroll(targetY, 900)
}

const handleWheel = (event) => {
  if (isScrolling.value) {
    event.preventDefault()
    return
  }

  if (Math.abs(event.deltaY) < 10) return

  event.preventDefault()

  if (event.deltaY > 0) {
    scrollToSection(currentSection.value + 1)
  } else {
    scrollToSection(currentSection.value - 1)
  }
}

const handleKeydown = (event) => {
  if (isScrolling.value) return

  if (
    event.key === 'ArrowDown' ||
    event.key === 'PageDown'
  ) {
    event.preventDefault()
    scrollToSection(currentSection.value + 1)
  }

  if (
    event.key === 'ArrowUp' ||
    event.key === 'PageUp'
  ) {
    event.preventDefault()
    scrollToSection(currentSection.value - 1)
  }

  if (event.key === 'Home') {
    event.preventDefault()
    scrollToSection(0)
  }

  if (event.key === 'End') {
    event.preventDefault()

    const sections = document.querySelectorAll('.home > section')

    scrollToSection(sections.length - 1)
  }
}

onMounted(() => {
  window.addEventListener('wheel', handleWheel, { passive: false })
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('wheel', handleWheel)
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
.home {
  width: 100%;
}


/* =========================
   HERO
   ========================= */

.hero {
  height: 100vh;
  min-height: 100vh;

  display: flex;
  align-items: center;

  padding: 80px 20px;

  background: #f1f8f5;
}

.hero-content {
  width: 100%;
  max-width: 900px;
  margin: 0 auto;

  text-align: left;
}

.hero h1 {
  max-width: 750px;

  margin: 0 0 22px;

  font-size: 52px;
  line-height: 1.15;

  color: #2c3e50;
}

.hero p {
  max-width: 700px;

  margin: 0 0 35px;

  font-size: 20px;
  line-height: 1.7;

  color: #667085;
}

.hero-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-primary,
.btn-secondary {
  display: inline-block;

  padding: 12px 24px;

  border-radius: 6px;

  font-weight: 600;
  text-decoration: none;

  transition: 0.2s;
}

.btn-primary {
  background: #42b883;
  color: white;
}

.btn-primary:hover {
  background: #369f6e;
}

.btn-secondary {
  background: white;
  color: #2c3e50;

  border: 1px solid #d0d5dd;
}

.btn-secondary:hover {
  background: #f8f9fa;
}


/* =========================
   ANALYZE SECTION
   ========================= */

.analyze-section {
  height: 100vh;
  min-height: 100vh;

  display: flex;
  align-items: center;

  padding: 80px 40px;

  background: white;
}

.analyze-wrapper {
  width: 100%;
  max-width: 1100px;

  margin: 0 auto;
}


/* =========================
   SECTION HEADING
   ========================= */

.section-heading {
  margin-bottom: 45px;
}

.section-heading h2 {
  margin: 0;

  color: #2c3e50;

  font-size: 48px;
  line-height: 1.15;
}

.section-line {
  width: 100%;
  height: 1px;

  margin-top: 25px;

  background: #d0d5dd;
}


/* =========================
   TWO-COLUMN CONTENT
   ========================= */

.analyze-content {
  display: grid;

  grid-template-columns: 1fr 1fr;

  gap: 80px;

  align-items: center;
}


/* =========================
   LEFT SIDE
   ========================= */

.feature-navigation {
  width: 100%;
}

.feature-list {
  display: flex;
  flex-direction: column;
}

.feature-tab {
  width: 100%;

  display: grid;
  grid-template-columns: 45px 1fr 25px;

  align-items: center;
  gap: 10px;

  padding: 28px 0;

  background: none;

  border: none;
  border-bottom: 1px solid #e5e7eb;

  text-align: left;

  cursor: pointer;

  color: #98a2b3;

  transition:
    color 0.35s ease,
    padding-left 0.35s ease;
}

.feature-tab:hover {
  color: #667085;
  padding-left: 6px;
}

.feature-tab.active {
  color: #2c3e50;
  padding-left: 14px;
}


/* Number */

.feature-number {
  font-size: 14px;
  font-weight: 600;

  color: #b0b7c3;

  transition:
    color 0.35s ease,
    transform 0.35s ease;
}

.feature-tab.active .feature-number {
  color: #42b883;

  transform: scale(1.1);
}


/* Title */

.feature-title {
  font-size: 19px;
  font-weight: 600;

  transition:
    transform 0.35s ease,
    color 0.35s ease;
}

.feature-tab.active .feature-title {
  color: #2c3e50;

  transform: scale(1.08);
  transform-origin: left center;
}


/* Arrow */

.feature-arrow {
  font-size: 22px;

  opacity: 0;

  transform: translateX(-8px);

  transition:
    opacity 0.3s ease,
    transform 0.3s ease;
}

.feature-tab:hover .feature-arrow,
.feature-tab.active .feature-arrow {
  opacity: 1;

  transform: translateX(0);
}


/* =========================
   RIGHT SIDE
   ========================= */

.feature-detail {
  min-height: 320px;

  display: flex;
  align-items: center;

  padding-left: 60px;

  border-left: 1px solid #d0d5dd;
}

.detail-number {
  margin-bottom: 18px;

  font-size: 15px;
  font-weight: 600;

  color: #42b883;
}

.feature-detail h3 {
  max-width: 500px;

  margin: 0 0 20px;

  font-size: 38px;
  line-height: 1.2;

  color: #2c3e50;
}

.feature-detail p {
  max-width: 500px;

  margin: 0;

  font-size: 20px;
  line-height: 1.7;

  color: #667085;
}


/* =========================
   FEATURE TRANSITION
   ========================= */

.feature-fade-enter-active,
.feature-fade-leave-active {
  transition:
    opacity 0.35s ease,
    transform 0.35s ease;
}

.feature-fade-enter-from {
  opacity: 0;

  transform: translateX(20px);
}

.feature-fade-leave-to {
  opacity: 0;

  transform: translateX(-20px);
}


/* =========================
   MOBILE
   ========================= */

@media (max-width: 800px) {
  .hero,
  .analyze-section {
    min-height: 100vh;
    height: auto;
  }

  .hero {
    min-height: 100vh;
  }

  .hero h1 {
    font-size: 40px;
  }

  .hero p {
    font-size: 18px;
  }

  .analyze-section {
    padding: 80px 25px;
  }

  .section-heading {
    margin-bottom: 35px;
  }

  .section-heading h2 {
    font-size: 38px;
  }

  .analyze-content {
    grid-template-columns: 1fr;

    gap: 45px;
  }

  .feature-detail {
    min-height: 250px;

    padding-left: 0;
    padding-top: 35px;

    border-left: none;
    border-top: 1px solid #d0d5dd;
  }

  .feature-detail h3 {
    font-size: 32px;
  }
}


/* =========================
   SMALL MOBILE
   ========================= */

@media (max-width: 600px) {
  .hero {
    padding: 70px 20px;
  }

  .hero h1 {
    font-size: 34px;
  }

  .hero p {
    font-size: 17px;
  }

  .hero-buttons {
    flex-direction: column;
    align-items: stretch;
  }

  .btn-primary,
  .btn-secondary {
    text-align: center;
  }

  .section-heading h2 {
    font-size: 34px;
  }

  .feature-title {
    font-size: 17px;
  }

  .feature-tab {
    grid-template-columns: 35px 1fr 20px;

    padding: 18px 0;
  }

  .feature-tab.active {
    padding-left: 8px;
  }

  .feature-tab.active .feature-title {
    transform: scale(1.04);
  }

  .feature-detail h3 {
    font-size: 28px;
  }

  .feature-detail p {
    font-size: 18px;
  }
}
</style>