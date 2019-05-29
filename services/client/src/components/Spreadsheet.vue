<template>
    <hot-table :data="data" :settings="hotSettings"></hot-table>
</template>

<script>
import { HotTable } from '@handsontable/vue';

export default {
  components: { HotTable },
  props: ['colnames'],
  data() {
    return {
      data: [[null, null]],
      hotSettings: {
        colHeaders: this.colnames,
        rowHeaders: true,
        height: 320,
        licenseKey: 'non-commercial-and-evaluation',
        columns: [
          {
            data: 'col0',
            type: 'numeric',
          },
          {
            data: 'col1',
            type: 'numeric',
          },
        ],
        afterChange() {
          const myData = this.getSourceDataArray();
          this.rootElement.__vue__.$emit('onChangeSheet', myData);
        },
      },
    };
  },
};
</script>

<style src="../../node_modules/handsontable/dist/handsontable.full.css"></style>
