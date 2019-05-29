<template>
    <hot-table :settings="hotSettings"></hot-table>
</template>

<script>
import { HotTable } from '@handsontable/vue';

export default {
  components: { HotTable },
  props: ['colnames'],
  data() {
    return {
      // data: [],
      hotSettings: {
        colHeaders: this.colnames,
        rowHeaders: true,
        startCols: 2,
        startRows: 1,
        minRows: 1,
        height: 320,
        licenseKey: 'non-commercial-and-evaluation',
        columns: [
          {
            type: 'numeric',
          },
          {
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
