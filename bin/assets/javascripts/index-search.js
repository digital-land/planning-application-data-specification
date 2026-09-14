export default function initIndexSearch({ form, count, noResults, elements, label, getText = element => element.textContent, renderItem = () => {} }) {
  const search = form.querySelector('input')
  const normalise = text => text.replace(/\s+/g, ' ').trim().toLowerCase()
  const items = [...elements].map(element => ({
    element,
    text: normalise(getText(element))
  }))

  function filterItems() {
    const term = normalise(search.value)
    let matches = 0
    items.forEach(item => {
      item.element.hidden = !item.text.includes(term)
      renderItem(item.element, term)
      if (!item.element.hidden) matches++
    })
    count.textContent = `Showing ${matches} of ${items.length} ${label}.`
    noResults.hidden = matches !== 0
  }

  search.addEventListener('input', filterItems)
  form.addEventListener('submit', event => {
    event.preventDefault()
    filterItems()
  })
  filterItems()
  form.hidden = false
}
