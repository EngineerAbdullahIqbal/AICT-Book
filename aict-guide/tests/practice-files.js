// Lessons that must offer practice files (specs/practical-upgrade/spec.md §3, PU-01).
// Add a lesson here FIRST (RED); then build its files with tools/practice-files and link them
// from the lesson with <PracticeFile> (GREEN). tools/practice-files/verify.py checks that the
// files and the page match and that every answer is right.
const xl = (slug) => `/module-07-ms-excel/${slug}`;

export const PRACTICE_LESSONS = [
  // Part 1: Excel Basics (7.1 has no data, so no files)
  'entering-editing-saving-data', 'rows-and-columns', 'formatting-cells', 'number-formats',
  'first-formulas', 'fill-handle', 'sum-and-average', 'min-max-count', 'sorting-data',
  'simple-chart', 'page-setup-and-printing', 'project-result-sheet',
  // Part 2: More Skills
  'absolute-references',
  'if-function',
  'ifs-and-or',
  'counting-functions',
  'sumif-sumifs-averageif',
  'vlookup-and-xlookup',
  'iferror-and-round',
  'rank-eq',
  'joining-and-changing-text',
  'parts-of-text',
  'working-with-dates',
  'sort-filter-unique',
  'filtering-data',
  'conditional-formatting',
  'freeze-panes',
  // Part 3: Real Projects
  'project-stock-and-sales',
  'project-customer-bill',
  'project-salary-sheet',
  'project-attendance-sheet',
  'project-result-card',
  'project-fee-record',
  'project-family-budget',
  'project-electricity-bill',
].map(xl);
