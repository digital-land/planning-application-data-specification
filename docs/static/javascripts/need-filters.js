// NeedFilters: simple checkbox-driven filtering for the needs list
// - Filters are defined by data-filter-name on the checkbox (e.g. data-filter-name="satisfied")
// - Checkbox values become URL params (e.g. ?satisfied=true)
// - Items carry data attributes (e.g. data-satisfied="true") for matching
// - On load, URL params pre-set filters and trigger filtering
// - Updates the "showing X" count

function NeedFilters($container, options = {}) {
  this.$container = $container
  this.$items = Array.from(document.querySelectorAll('[data-need-item]'))
  this.countWrapperSelector = options.count_wrapper_selector || '.js-list-filter__count'
  this.$countWrapper = document.querySelector(this.countWrapperSelector)
  this.filters = Array.from(
    $container.querySelectorAll('input[type="checkbox"][data-filter-name]')
  )
}

NeedFilters.prototype.init = function () {
  if (!this.$container) return
  this.applyParamsFromUrl()
  this.bindEvents()
  this.filter()
}

NeedFilters.prototype.bindEvents = function () {
  const self = this
  this.filters.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
      self.updateUrl()
      self.filter()
    })
  })
}

NeedFilters.prototype.getActiveFilters = function () {
  const active = {}
  this.filters.forEach(function (cb) {
    const name = cb.dataset.filterName
    if (cb.checked) {
      active[name] = active[name] || []
      active[name].push(cb.value)
    }
  })
  return active
}

NeedFilters.prototype.filter = function () {
  const active = this.getActiveFilters()
  let visibleCount = 0

  this.$items.forEach(function (item) {
    const matches = Object.keys(active).every(function (filterName) {
      const attr = item.dataset[filterName.replace(/-([a-z])/g, (m, p1) => p1.toUpperCase())]
      if (attr === undefined) return false
      return active[filterName].includes(attr)
    })
    if (matches) {
      item.classList.remove('js-hidden')
      visibleCount += 1
    } else {
      item.classList.add('js-hidden')
    }
  })

  if (this.$countWrapper) {
    const live = this.$countWrapper.querySelector('.js-list-filter__count')
    const accessible = this.$countWrapper.querySelector('.js-accessible-list-filter__count')
    if (live) live.textContent = visibleCount
    if (accessible) accessible.textContent = visibleCount
  }
}

NeedFilters.prototype.updateUrl = function () {
  const params = new URLSearchParams(window.location.search)
  // clear relevant params
  this.filters.forEach(function (cb) {
    params.delete(cb.dataset.filterName)
  })
  // set active params
  const active = this.getActiveFilters()
  Object.keys(active).forEach(function (name) {
    active[name].forEach(function (val) {
      params.append(name, val)
    })
  })
  const newUrl = window.location.pathname + (params.toString() ? '?' + params.toString() : '')
  window.history.replaceState({}, '', newUrl)
}

NeedFilters.prototype.applyParamsFromUrl = function () {
  const params = new URLSearchParams(window.location.search)
  this.filters.forEach(function (cb) {
    const name = cb.dataset.filterName
    const values = params.getAll(name)
    cb.checked = values.includes(cb.value)
  })
}

export default NeedFilters
