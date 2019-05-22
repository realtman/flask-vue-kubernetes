<template>
    <hot-table :settings="hotSettings"></hot-table>
</template>

<script>
import { HotTable } from '@handsontable/vue';

export default {
  components: { HotTable },
  props: ['columnNames'],
  data() {
    return {
      hotSettings: {
        data: [['', '']],
        colHeaders: this.columnNames,
        rowHeaders: true,
        // autoColumnSize: true,
        height: 320,
        // colWidths: [150, 200],
        licenseKey: 'non-commercial-and-evaluation',
      },
    };
  },
  methods: {
    setData(data) {
      this.$refs.hotTableComponent.hotInstance.loadData(data);
    }
  },
};
</script>

<style src="../../node_modules/handsontable/dist/handsontable.full.css"></style>
