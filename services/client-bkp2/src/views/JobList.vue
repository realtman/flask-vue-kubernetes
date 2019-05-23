<template>
<div>
    <TitleComponent :title="'Job List'" :subtitle="'overview'">
    </TitleComponent>
    <TableComponent :columns="['ColumnOne', 'ColumnTwo']" :rows='[ { "ColumnOne": { "type": "text", "data": "a" }, "ColumnTwo": { "type": "text", "data": "Value1" } }, { "ColumnOne": { "type": "text", "data": "b" }, "ColumnTwo": { "type": "text", "data": "Value11" } } ]'>
    </TableComponent>
</div>
</template>

<script>
import TitleComponent from '../components/Title.vue'
import TableComponent from '../components/Table.vue'
export default {
    name: 'CCD',
    components: {
        TitleComponent,
        TableComponent
    }
}
</script>
