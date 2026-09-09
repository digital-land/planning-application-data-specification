// One controller owns facets, search and browser history.
export default class NeedFilters {
  constructor(container) {
    this.container = container
    this.inputs = [...container.querySelectorAll('[data-filter-name]')]
    this.search = document.querySelector('#filter-needs-list')
    this.names = [...new Set(this.inputs.map(input => input.dataset.filterName))]
    this.items = [...document.querySelectorAll('[data-need-item]')].map(element => ({
      element,
      text: (element.querySelector('[data-filter="match-content"]').textContent + ' ' + element.dataset.reference).toLowerCase(),
      scope: [element.dataset.scope], satisfaction: [element.dataset.satisfaction],
      theme: JSON.parse(element.dataset.theme), actor: JSON.parse(element.dataset.actor)
    }))
  }
  init() {
    this.restore()
    this.writeUrl('replaceState')
    this.container.hidden = false
    this.search.closest('form').hidden = false
    this.container.addEventListener('change', event => {
      if (event.target.matches('[data-filter-name]')) this.commit()
    })
    this.search.addEventListener('input', () => {
      this.render()
      clearTimeout(this.timer)
      this.timer = setTimeout(() => this.commit(), 500)
    })
    this.search.closest('form').addEventListener('submit', event => { event.preventDefault(); this.commit() })
    this.container.addEventListener('submit', event => event.preventDefault())
    this.container.querySelector('[data-clear-filters]').addEventListener('click', () => {
      this.inputs.forEach(input => { input.checked = false })
      this.commit()
    })
    window.addEventListener('popstate', () => { clearTimeout(this.timer); this.restore() })
  }
  restore() {
    const params = new URLSearchParams(window.location.search)
    this.search.value = params.get('list_filter') || ''
    this.inputs.forEach(input => {
      const name = input.dataset.filterName
      let values = params.getAll(name)
      if (name === 'scope' && !params.has('scope')) values = ['in']
      if (name === 'satisfaction' && !params.has(name) && params.has('satisfied')) {
        values = params.getAll('satisfied').flatMap(value => value === 'true' ? ['full'] : value === 'false' ? ['partial', 'none'] : [])
      }
      input.checked = values.includes(input.value)
    })
    this.render()
  }
  active() {
    return Object.fromEntries(this.names.map(name => [name, this.inputs.filter(input => input.dataset.filterName === name && input.checked).map(input => input.value)]))
  }
  commit() {
    clearTimeout(this.timer)
    this.render()
    this.writeUrl('pushState')
  }
  writeUrl(method) {
    const url = new URL(window.location.href)
    const active = this.active()
    ;[...this.names, 'satisfied', 'list_filter'].forEach(name => url.searchParams.delete(name))
    Object.entries(active).forEach(([name, values]) => values.forEach(value => url.searchParams.append(name, value)))
    // Explicit all preserves a cleared scope selection on reload.
    if (!active.scope.length) url.searchParams.set('scope', 'all')
    if (this.search.value) url.searchParams.set('list_filter', this.search.value)
    if (url.href !== window.location.href) window.history[method]({}, '', url)
  }
  render() {
    const active = this.active()
    const term = this.search.value.trim().toLowerCase()
    let count = 0
    this.items.forEach(item => {
      const matches = this.names.every(name => !active[name].length || active[name].some(value => item[name].includes(value))) && item.text.includes(term)
      item.element.hidden = !matches
      if (matches) count++
    })
    document.querySelector('[data-needs-count]').textContent = `Showing ${count} of ${this.items.length} needs`
    document.querySelector('[data-no-needs]').hidden = count !== 0
    const selected = this.container.querySelector('[data-selected-filters]')
    selected.replaceChildren()
    this.inputs.filter(input => input.checked).forEach(input => {
      const button = document.createElement('button')
      button.type = 'button'
      button.className = 'govuk-link app-remove-filter'
      const label = input.labels[0].textContent.trim()
      const visibleLabel = document.createElement('span')
      visibleLabel.setAttribute('aria-hidden', 'true')
      visibleLabel.textContent = label + ' ×'
      const accessibleLabel = document.createElement('span')
      accessibleLabel.className = 'govuk-visually-hidden'
      accessibleLabel.textContent = 'Remove ' + label + ' filter'
      button.append(visibleLabel, accessibleLabel)
      button.addEventListener('click', () => {
        input.checked = false
        this.commit()
        input.closest('details').querySelector('summary').focus()
      })
      const item = document.createElement('li')
      item.append(button)
      selected.append(item)
    })
    this.container.querySelectorAll('[data-facet-count]').forEach(span => { span.textContent = active[span.dataset.facetCount].length })
    // Refresh the reused checkbox-option search counts after URL restoration
    // or removing selections without a checkbox change event.
    this.container.querySelectorAll('.dl-filter-group__auto-filter__input').forEach(input => {
      input.dispatchEvent(new Event('input', { bubbles: true }))
    })
  }
}
