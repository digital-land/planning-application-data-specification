const form = document.querySelector('[data-fields-search]')
const search = form.querySelector('input')
const count = document.querySelector('[data-fields-count]')
const noResults = document.querySelector('[data-no-fields]')
const normalise = text => text.replace(/\s+/g, ' ').trim().toLowerCase()
const items = [...document.querySelectorAll('[data-field-item]')].map(element => ({
  element,
  text: normalise(element.textContent)
}))

function filterFields() {
  const term = normalise(search.value)
  let matches = 0
  items.forEach(item => {
    item.element.hidden = !item.text.includes(term)
    if (!item.element.hidden) matches++
  })
  count.textContent = `Showing ${matches} of ${items.length} fields.`
  noResults.hidden = matches !== 0
}

search.addEventListener('input', filterFields)
form.addEventListener('submit', event => {
  event.preventDefault()
  filterFields()
})
filterFields()
form.hidden = false
