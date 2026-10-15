// Lessons per module, in teaching order. Each lesson task adds its entry FIRST (RED),
// before the lesson is written. See specs/module-*/tasks.md.
const lesson = (module, slug, title) => ({url: `/${module}/${slug}`, title});

const M1 = 'module-01-computer-basics';
const M2 = 'module-02-typing-skills';
const M4 = 'module-04-ms-word';
const M5 = 'module-05-ms-powerpoint';
const M6 = 'module-06-presentation-skills';
const M7 = 'module-07-ms-excel';

export const MODULE_LESSONS = {
  [M1]: [
    lesson(M1, 'what-is-a-computer', 'Lesson 1.1: What Is a Computer? Input, Processing, Output and Storage'),
    lesson(M1, 'hardware-and-software', 'Lesson 1.2: Hardware and Software'),
    lesson(M1, 'parts-of-a-computer', 'Lesson 1.3: Parts of a Computer and Their Jobs'),
    lesson(M1, 'starting-up-and-shutting-down', 'Lesson 1.4: Starting Up and Shutting Down Safely'),
    lesson(M1, 'using-the-mouse', 'Lesson 1.5: Using the Mouse'),
    lesson(M1, 'keyboard-basics', 'Lesson 1.6: Keyboard Basics'),
    lesson(M1, 'operating-system-and-desktop', 'Lesson 1.7: The Operating System and the Desktop'),
    lesson(M1, 'files-folders-saving-deleting', 'Lesson 1.8: Files, Folders, Saving and Deleting'),
    lesson(M1, 'caring-for-your-computer', 'Lesson 1.9: Caring for Your Computer'),
  ],
  [M2]: [
    lesson(M2, 'sitting-right-and-home-row', 'Lesson 2.1: Sitting Right and the Home Row'),
    lesson(M2, 'home-row-keys', 'Lesson 2.2: Typing the Home Row Keys'),
    lesson(M2, 'top-row', 'Lesson 2.3: The Top Row'),
    lesson(M2, 'bottom-row', 'Lesson 2.4: The Bottom Row'),
    lesson(M2, 'capitals-and-punctuation', 'Lesson 2.5: Capital Letters and Punctuation'),
    lesson(M2, 'number-row', 'Lesson 2.6: The Number Row'),
    lesson(M2, 'words-and-sentences', 'Lesson 2.7: Typing Words and Sentences'),
    lesson(M2, 'speed-and-accuracy', 'Lesson 2.8: Measuring Your Speed and Accuracy'),
    lesson(M2, 'project-real-paragraph', 'Lesson 2.9: Project: Type a Real Paragraph'),
  ],
  [M4]: [
    lesson(M4, 'starting-word', 'Lesson 4.1: Starting Word and the Word Window'),
    lesson(M4, 'typing-and-correcting-text', 'Lesson 4.2: Typing and Correcting Text'),
    lesson(M4, 'saving-closing-opening', 'Lesson 4.3: Saving, Closing and Opening a Document'),
    lesson(M4, 'copy-cut-paste', 'Lesson 4.4: Selecting Text: Copy, Cut and Paste'),
    lesson(M4, 'formatting-text', 'Lesson 4.5: Formatting Text: Font, Size and Style'),
    lesson(M4, 'formatting-paragraphs', 'Lesson 4.6: Formatting Paragraphs: Alignment and Line Spacing'),
    lesson(M4, 'bulleted-and-numbered-lists', 'Lesson 4.7: Bulleted and Numbered Lists'),
    lesson(M4, 'spelling-and-grammar', 'Lesson 4.8: Checking Spelling and Grammar'),
    lesson(M4, 'tables', 'Lesson 4.9: Tables'),
    lesson(M4, 'pictures-and-shapes', 'Lesson 4.10: Pictures and Shapes'),
    lesson(M4, 'page-setup-and-printing', 'Lesson 4.11: Page Setup and Printing'),
    lesson(M4, 'project-application-letter', 'Lesson 4.12: Project: A Job Application Letter'),
    lesson(M4, 'project-cv', 'Lesson 4.13: Project: Your CV'),
  ],
  [M5]: [
    lesson(M5, 'starting-powerpoint', 'Lesson 5.1: Starting PowerPoint and the PowerPoint Window'),
    lesson(M5, 'adding-slides-and-text', 'Lesson 5.2: Adding Slides and Typing Text'),
    lesson(M5, 'saving-and-slide-show', 'Lesson 5.3: Saving, Opening and Showing a Slide Show'),
    lesson(M5, 'formatting-text-on-slides', 'Lesson 5.4: Formatting Text on Slides'),
    lesson(M5, 'design-themes', 'Lesson 5.5: Design Themes'),
    lesson(M5, 'pictures-and-shapes', 'Lesson 5.6: Pictures and Shapes on Slides'),
    lesson(M5, 'tables-and-charts', 'Lesson 5.7: Tables and Charts on Slides'),
    lesson(M5, 'organizing-slides', 'Lesson 5.8: Organizing Slides'),
    lesson(M5, 'slide-transitions', 'Lesson 5.9: Slide Transitions'),
    lesson(M5, 'simple-animations', 'Lesson 5.10: Simple Animations'),
    lesson(M5, 'speaker-notes-and-printing', 'Lesson 5.11: Speaker Notes and Printing'),
    lesson(M5, 'project-shop-presentation', 'Lesson 5.12: Project: A Presentation for a Real Purpose'),
  ],
  [M6]: [
    lesson(M6, 'what-makes-a-good-presentation', 'Lesson 6.1: What Makes a Good Presentation'),
    lesson(M6, 'planning-your-talk', 'Lesson 6.2: Planning Your Talk: Beginning, Middle and End'),
    lesson(M6, 'slides-that-help', 'Lesson 6.3: Slides That Help You Speak'),
    lesson(M6, 'your-voice', 'Lesson 6.4: Your Voice: Speaking Clearly'),
    lesson(M6, 'body-language-and-eye-contact', 'Lesson 6.5: Body Language and Eye Contact'),
    lesson(M6, 'handling-nervousness', 'Lesson 6.6: Handling Nervousness'),
    lesson(M6, 'practising-with-powerpoint', 'Lesson 6.7: Practising With PowerPoint: Notes, Timings and Presenter View'),
    lesson(M6, 'answering-questions', 'Lesson 6.8: Answering Questions'),
    lesson(M6, 'project-three-minute-talk', 'Lesson 6.9: Project: Give a 3-Minute Presentation'),
  ],
  [M7]: [
    lesson(M7, 'starting-excel', 'Lesson 7.1: Starting Excel: Workbooks, Worksheets and Cells'),
    lesson(M7, 'entering-editing-saving-data', 'Lesson 7.2: Entering, Editing and Saving Data'),
    lesson(M7, 'rows-and-columns', 'Lesson 7.3: Rows and Columns: Width, Height, Insert and Delete'),
    lesson(M7, 'formatting-cells', 'Lesson 7.4: Formatting Cells: Font, Fill, Borders and Alignment'),
    lesson(M7, 'number-formats', 'Lesson 7.5: Number Formats: Money, Percentages and Dates'),
    lesson(M7, 'first-formulas', 'Lesson 7.6: Your First Formulas'),
    lesson(M7, 'fill-handle', 'Lesson 7.7: Copying Formulas with the Fill Handle'),
    lesson(M7, 'sum-and-average', 'Lesson 7.8: Functions: SUM and AVERAGE'),
    lesson(M7, 'min-max-count', 'Lesson 7.9: Functions: MIN, MAX and COUNT'),
    lesson(M7, 'sorting-data', 'Lesson 7.10: Sorting Data'),
    lesson(M7, 'simple-chart', 'Lesson 7.11: Making a Simple Chart'),
    lesson(M7, 'page-setup-and-printing', 'Lesson 7.12: Page Setup and Printing a Worksheet'),
    lesson(M7, 'project-result-sheet', 'Lesson 7.13: Project: Student Result Sheet'),
  ],
};

export const LESSONS = Object.values(MODULE_LESSONS).flat();
