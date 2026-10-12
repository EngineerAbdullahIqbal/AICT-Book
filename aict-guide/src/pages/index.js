// The book's front page (specs/site-design/spec.md §3).
// Layout and style follow the reference design; all text and branding are our own.
import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import {usePluginData} from '@docusaurus/useGlobalData';
import useBrokenLinks from '@docusaurus/useBrokenLinks';
import styles from './index.module.css';

// The 16 modules in course order (specs/book-spec.md §3), with a short line for each card.
const MODULES = [
  ['module-01-computer-basics', 'Computer Basics', 'The parts of a computer, the mouse, the keyboard and saving files.'],
  ['module-02-typing-skills', 'Typing Skills', 'Type faster and with fewer mistakes.'],
  ['module-03-internet-essentials', 'Internet Essentials', 'Use the web and email safely.'],
  ['module-04-ms-word', 'MS Word', 'Write, format and print letters and a CV.'],
  ['module-05-ms-powerpoint', 'MS PowerPoint', 'Make slides with text and pictures.'],
  ['module-06-presentation-skills', 'Presentation Skills', 'Speak with confidence in front of a group.'],
  ['module-07-ms-excel', 'MS Excel', 'Keep records and do sums with formulas and charts.'],
  ['module-08-inpage-urdu', 'InPage Urdu', 'Type and design pages in Urdu.'],
  ['module-09-google-workspace', 'Google Workspace', 'Work online with Google tools.'],
  ['module-10-ai-basics', 'AI Basics', 'What AI is and how to use AI tools well.'],
  ['module-11-html-css', 'HTML & CSS', 'Build your first simple web page.'],
  ['module-12-adobe-photoshop', 'Adobe Photoshop', 'Edit and improve photos.'],
  ['module-13-adobe-illustrator', 'Adobe Illustrator', 'Draw logos and simple pictures.'],
  ['module-14-canva', 'Canva', 'Design posters and social media posts.'],
  ['module-15-social-media-marketing', 'Social Media Marketing', 'Grow a business with social media.'],
  ['module-16-freelancing-intro', 'Freelancing Intro', 'Find online work and get paid.'],
];

// The class plan for one lesson (specs/book-spec.md §4).
const LESSON_STEPS = [
  ['Goal and Key Terms', 'What you will learn today, and the new words.', '10 minutes'],
  ['Teacher Demo', 'The teacher shows each step on the big screen.', '15 minutes'],
  ['Student Task', 'You do the same steps on your own computer.', '25 minutes'],
  ['Check Questions', 'Three questions to check what you learned.', '10 minutes'],
];

// Count the lessons in each module from the docs plugin's data, so "Ready" and the
// lesson count update by themselves when lessons are added.
function useLessonCounts() {
  const docsData = usePluginData('docusaurus-plugin-content-docs');
  const docs = docsData.versions[0].docs;
  const counts = {};
  for (const {id} of docs) {
    const [folder, page] = id.split('/');
    if (page && page !== 'index') {
      counts[folder] = (counts[folder] ?? 0) + 1;
    }
  }
  return counts;
}

// A section that other pages link to by its id (/#modules). Registering the id lets the
// build's broken-anchor check find it (Docusaurus docs: useBrokenLinks).
function AnchoredSection({id, className, children}) {
  useBrokenLinks().collectAnchor(id);
  return (
    <section id={id} className={className}>
      {children}
    </section>
  );
}

function Eyebrow({children}) {
  return <p className={styles.eyebrow}>{children}</p>;
}

function BookCover() {
  return (
    <div className={styles.coverWrap} aria-hidden="true">
      <div className={styles.cover}>
        <div className={styles.coverTop}>
          <span>GLOBAL COACHING CENTER</span>
          <span>1-YEAR COURSE</span>
        </div>
        <svg className={styles.coverArt} viewBox="0 0 240 120">
          <rect x="20" y="20" width="80" height="54" />
          <rect x="52" y="74" width="16" height="10" />
          <rect x="38" y="84" width="44" height="6" />
          <rect x="130" y="20" width="90" height="70" />
          <path d="M130 38h90M130 56h90M130 74h90M160 20v70M190 20v70" />
          <path d="M100 47h30" className={styles.coverLink} />
          <circle cx="115" cy="47" r="4" />
        </svg>
        <p className={styles.coverKicker}>WORD · EXCEL · INTERNET · DESIGN</p>
        <p className={styles.coverTitle}>
          AICT
          <br />
          COURSE
          <br />
          <span>GUIDE</span>
        </p>
        <p className={styles.coverTagline}>A one-year computer course for complete beginners.</p>
        <p className={styles.coverFoot}>LEARN STEP BY STEP · ONE CLASS AT A TIME</p>
      </div>
    </div>
  );
}

function Hero({lessonsReady}) {
  return (
    <header className={styles.hero}>
      <div className={styles.heroText}>
        <p className={styles.badge}>
          <span className={styles.badgeTag}>NEW</span>
          Word and Excel modules are ready to teach
        </p>
        <h1 className={styles.heroTitle}>
          <span>AICT</span> <span className={styles.accent}>Course Guide</span>
        </h1>
        <p className={styles.heroLead}>
          A <strong>one-year computer course</strong> for complete beginners. Learn to use a
          computer, write letters in <strong>Word</strong>, work with numbers in{' '}
          <strong>Excel</strong>, and much more.
        </p>
        <p className={styles.heroSub}>
          By <strong>Global Coaching Center</strong>. Made for the classroom: your teacher shows
          each lesson on the big screen, and you practise step by step on your own computer.
        </p>
        <div className={styles.actions}>
          <Link className={styles.btnPrimary} to="/start">
            Start Reading →
          </Link>
          <Link className={styles.btnOutline} to="/#modules">
            See the Modules
          </Link>
          <Link className={styles.btnText} to="/#how-it-works">
            How it works ↓
          </Link>
        </div>
        <p className={styles.stats}>
          <span className={styles.statDot} />
          <strong>{lessonsReady}</strong> lessons ready
          <span className={styles.statSep} />
          <strong>16</strong> modules
          <span className={styles.statSep} />
          <strong>1</strong> year
        </p>
      </div>
      <BookCover />
    </header>
  );
}

function AtAGlance({lessonsReady}) {
  const facts = [
    ['16', 'Modules', 'From your first mouse click to finding online work.'],
    ['1', 'Year', 'One module after another, in a clear order.'],
    ['60', 'Minutes', 'Every lesson fits one class.'],
    [String(lessonsReady), 'Lessons ready', 'More lessons are added as the course goes on.'],
  ];
  return (
    <section className={styles.band}>
      <div className={styles.bandInner}>
        <div>
          <Eyebrow>AT A GLANCE</Eyebrow>
          <h2 className={styles.bigTitle}>
            Learn computers
            <br />
            <span className={styles.accent}>from zero.</span>
          </h2>
          <p className={styles.bandText}>
            You do not need to know anything about computers to start. Every new word is
            explained, and every step is shown.
          </p>
        </div>
        <div className={styles.factGrid}>
          {facts.map(([value, label, text]) => (
            <div key={label} className={styles.fact}>
              <p className={styles.factValue}>{value}</p>
              <p className={styles.factLabel}>{label}</p>
              <p className={styles.factText}>{text}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function ModuleCards({counts}) {
  return (
    <AnchoredSection id="modules" className={styles.section}>
      <div className={styles.sectionHead}>
        <Eyebrow>THE COURSE</Eyebrow>
        <h2 className={styles.sectionTitle}>The 16 Modules</h2>
        <p className={styles.sectionLead}>
          Follow them in order. Modules marked <strong>Ready</strong> have lessons you can use
          today.
        </p>
      </div>
      <div className={styles.moduleGrid}>
        {MODULES.map(([folder, name, line], i) => {
          const lessons = counts[folder] ?? 0;
          const ready = lessons > 0;
          return (
            <Link
              key={folder}
              to={`/${folder}`}
              data-module-card
              className={`${styles.moduleCard} ${ready ? styles.moduleReady : ''}`}>
              <div className={styles.moduleTop}>
                <span className={styles.moduleNum}>{String(i + 1).padStart(2, '0')}</span>
                <span className={ready ? styles.tagReady : styles.tagSoon}>
                  {ready ? 'Ready' : 'Coming soon'}
                </span>
              </div>
              <h3 className={styles.moduleName}>{name}</h3>
              <p className={styles.moduleLine}>{line}</p>
              <p className={styles.moduleMeta}>
                {ready ? `${lessons} lessons →` : 'Lessons coming soon'}
              </p>
            </Link>
          );
        })}
      </div>
    </AnchoredSection>
  );
}

function HowItWorks() {
  return (
    <AnchoredSection id="how-it-works" className={styles.section}>
      <div className={styles.sectionHead}>
        <Eyebrow>HOW EVERY LESSON WORKS</Eyebrow>
        <h2 className={styles.sectionTitle}>One Lesson, One Class</h2>
        <p className={styles.sectionLead}>
          Every lesson has the same parts, in the same order. You always know what comes next.
        </p>
      </div>
      <ol className={styles.steps}>
        {LESSON_STEPS.map(([title, text, time], i) => (
          <li key={title} className={styles.step}>
            <span className={styles.stepNum}>{i + 1}</span>
            <div className={styles.stepBody}>
              <h3 className={styles.stepTitle}>{title}</h3>
              <p className={styles.stepText}>{text}</p>
            </div>
            <span className={styles.stepTime}>{time}</span>
          </li>
        ))}
      </ol>
    </AnchoredSection>
  );
}

function Audiences() {
  const cards = [
    {
      title: 'For Teachers',
      sub: 'TEACH FROM THE BIG SCREEN',
      text: 'Open the lesson on the projector and follow the Teacher Demo out loud.',
      points: [
        'Clear steps, one action at a time',
        'Common Mistakes help you correct students',
        'Steps to test before class are clearly marked',
      ],
      example: 'Show Lesson 7.8, add a SUM formula, and the class sees the answer appear.',
    },
    {
      title: 'For Students',
      sub: 'PRACTISE AND REVISE',
      text: 'Do the Student Task on your own computer, then check yourself.',
      points: [
        'Key Terms explain every new word',
        'Practice tables you type yourself',
        'Check Questions with answers for revision',
      ],
      example: 'Type the shop price list, then show your teacher your finished table.',
    },
  ];
  return (
    <section className={styles.section}>
      <div className={styles.sectionHead}>
        <Eyebrow>ONE BOOK, TWO USES</Eyebrow>
        <h2 className={styles.sectionTitle}>For Teachers and Students</h2>
      </div>
      <div className={styles.audienceGrid}>
        {cards.map((card, i) => (
          <div key={card.title} className={`${styles.audience} ${i === 1 ? styles.audienceHi : ''}`}>
            <h3 className={styles.audienceTitle}>{card.title}</h3>
            <p className={styles.audienceSub}>{card.sub}</p>
            <p className={styles.audienceText}>{card.text}</p>
            <ul className={styles.audienceList}>
              {card.points.map((point) => (
                <li key={point}>{point}</li>
              ))}
            </ul>
            <p className={styles.audienceExample}>
              <strong>Example:</strong> {card.example}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}

function StartCall() {
  return (
    <section className={styles.cta}>
      <div>
        <h2 className={styles.ctaTitle}>Ready to Start?</h2>
        <p className={styles.ctaText}>
          Begin with Module 1. You will turn on a computer, use the mouse and the keyboard, and
          save your first file.
        </p>
        <div className={styles.actions}>
          <Link className={styles.btnPrimary} to="/module-01-computer-basics">
            Start with Module 1 →
          </Link>
          <Link className={styles.btnOutline} to="/start">
            How to Use This Book
          </Link>
        </div>
      </div>
      <div className={styles.window} aria-hidden="true">
        <div className={styles.windowBar}>
          <span className={styles.dotRed} />
          <span className={styles.dotYellow} />
          <span className={styles.dotGreen} />
          <span className={styles.windowName}>Lesson 1.1</span>
        </div>
        <div className={styles.windowBody}>
          <p>
            <span className={styles.accent}>Goal:</span> name the four jobs of a computer
          </p>
          <p className={styles.dim}>▸ Input → Processing → Output → Storage</p>
          <p className={styles.ok}>✓ Show your teacher: your answers</p>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const counts = useLessonCounts();
  const lessonsReady = Object.values(counts).reduce((sum, n) => sum + n, 0);
  return (
    <Layout
      title="A one-year computer course for complete beginners"
      description="AICT Course Guide by Global Coaching Center: a one-year computer course for complete beginners.">
      <main className={styles.page}>
        <Hero lessonsReady={lessonsReady} />
        <AtAGlance lessonsReady={lessonsReady} />
        <ModuleCards counts={counts} />
        <HowItWorks />
        <Audiences />
        <StartCall />
      </main>
    </Layout>
  );
}
