<template>
<!-- Card -->
<div class="card" data-toggle="lists">
    <div class="card-header">
        <div class="row align-items-center">
            <div class="col">

                <!-- Search -->
                <form class="row align-items-center">
                    <div class="col-auto pr-0">
                        <span class="fe fe-search text-muted"></span>
                    </div>
                    <div class="col">
                        <input type="search" class="form-control form-control-flush search" placeholder="Search" v-model="filterKey">
                    </div>
                </form>
            </div>
        </div> <!-- / .row -->
    </div>
    <div class="table-responsive">
        <table class="table table-sm table-nowrap card-table">
            <thead>
                <tr>
                    <th v-for="key in columns" v-bind:key="key" @click="sortBy(key)" :class="{ active: sortKey == key }">
                        <a href="#" class="text-muted sort">
                            {{key | capitalize}}
                        </a>
                    </th>
                </tr>
            </thead>
            <tbody class="list">
                <tr v-for="row in filterRows" v-bind:key="row.index">
                    <td v-for="key in columns" v-bind:key="key">
                        <div class="badge badge-soft-success" v-if="row[key].type == 'status-green'">
                            {{row[key].data}}
                        </div>
                        <div class="badge badge-soft-warning" v-else-if="row[key].type == 'status-yellow'">
                            {{row[key].data}}
                        </div>
                        <div class="badge badge-soft-danger" v-else-if="row[key].type == 'status-red'">
                            {{row[key].data}}
                        </div>
                        <div v-else-if="row[key].type == 'date'">
                            <time>{{row[key].data}}</time>
                        </div>
                        <div v-else-if="row[key].type == 'text'">
                            {{row[key].data}}
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</template>

<script>
export default {
    name: 'inari-table',
    props: {
        columns: Array,
        rows: Array,
        
    },
    data: function () {
        var sortOrders = {}
        this.columns.forEach(function (key) {
            sortOrders[key] = 1
        })
        return {
            sortKey: '',
            message: '',
            filterKey: '',
            sortOrders: sortOrders
        }
    },
    computed: {
        filterRows: function () {
            var sortKey = this.sortKey
            var filterKey = this.filterKey && this.filterKey.toLowerCase()
            var order = this.sortOrders[sortKey] || 1
            var rows = this.rows
            if (filterKey) {
                rows = rows.filter(function (row) {
                    return Object.keys(row).some(function (key) {
                        return Object.keys(row[key]).some(function (innerKey) {
                            return String(row[key][innerKey]).toLowerCase().indexOf(filterKey) > -1
                        })
                    })
                })
            }
            if (sortKey) {
                rows = rows.slice().sort(function (a, b) {
                    a = a[sortKey]['data']
                    b = b[sortKey]['data']
                    return (a === b ? 0 : a > b ? 1 : -1) * order
                })
            }
            return rows
        }
    },
    filters: {
        capitalize: function (str) {
            return str.charAt(0).toUpperCase() + str.slice(1)
        }
    },
    methods: {
        sortBy: function (key) {
            this.sortKey = key
            this.sortOrders[key] = this.sortOrders[key] * -1
        }
    }

}
</script>
