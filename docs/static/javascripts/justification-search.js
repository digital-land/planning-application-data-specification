import initIndexSearch from './index-search.js'

const elements = [...document.querySelectorAll('[data-justification-item]')]
const records = new Map(elements.map(element => [element, {
  body: element.dataset.searchBody.replace(/\s+/g, ' ').trim(),
  references: JSON.parse(element.dataset.searchReferences)
}]))

function excerpt(text, term) {
  const index = text.toLowerCase().indexOf(term)
  if (index === -1) return ''
  let start = Math.max(0, index - 70)
  let end = Math.min(text.length, index + term.length + 110)
  if (start > 0) {
    const boundary = text.indexOf(' ', start)
    if (boundary < index) start = boundary + 1
  }
  if (end < text.length) {
    const boundary = text.lastIndexOf(' ', end)
    if (boundary >= index + term.length) end = boundary
  }
  return (start ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '')
}

initIndexSearch({
  form: document.querySelector('[data-justifications-search]'),
  count: document.querySelector('[data-justifications-count]'),
  noResults: document.querySelector('[data-no-justifications]'),
  elements,
  label: 'justifications',
  getText(element) {
    const record = records.get(element)
    return `${element.textContent} ${record.body} ${record.references.join(' ')}`
  },
  renderItem(element, term) {
    const record = records.get(element)
    const body = element.querySelector('[data-search-excerpt]')
    const references = element.querySelector('[data-search-reference-match]')
    body.textContent = term ? excerpt(record.body, term) : ''
    references.textContent = term ? record.references.filter(ref => ref.toLowerCase().includes(term)).join('; ') : ''
    body.hidden = !body.textContent
    references.hidden = !references.textContent
  }
})
