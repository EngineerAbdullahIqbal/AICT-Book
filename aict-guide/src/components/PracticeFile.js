// A download link for a practice file in static/files/ (specs/practical-upgrade/spec.md §3).
// A plain Markdown link would let the bundler rename the file (e.g. marks-starter-4dd9….xlsx);
// this keeps the real file name and adds the site's baseUrl (Docusaurus: useBaseUrl).
import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function PracticeFile({href, children}) {
  const url = useBaseUrl(href);
  const name = href.split('/').pop();
  return (
    <a href={url} download={name}>
      {children}
    </a>
  );
}
