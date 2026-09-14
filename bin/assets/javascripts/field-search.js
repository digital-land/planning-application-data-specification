import initIndexSearch from './index-search.js'

initIndexSearch({
  form: document.querySelector('[data-fields-search]'),
  count: document.querySelector('[data-fields-count]'),
  noResults: document.querySelector('[data-no-fields]'),
  elements: document.querySelectorAll('[data-field-item]'),
  label: 'fields'
})
