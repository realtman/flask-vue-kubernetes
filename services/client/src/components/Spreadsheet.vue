<template>
    <hot-table ref="mytable" :settings="hotSettings"></hot-table>
</template>

<script>
import { HotTable } from '@handsontable/vue';

export default {
  components: { HotTable },
  props: ['colnames', 'value'],
  data() {
    return {
      data: this.value,
      hotSettings: {
        colHeaders: this.colnames,
        rowHeaders: true,
        startCols: 2,
        startRows: 1,
        minRows: 1,
        stretchH: 'all',
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
        // afterListen() {
        //   alert(this.value);
        //   this.loadData(this.value);
        // },
        afterChange(change, source) {
          if (source === 'loadData') {
              return; //don't save this change
          }
          const myData = this.getSourceDataArray();
          this.rootElement.__vue__.$emit('onChangeSheet', myData);
        },
      },
    };
  },
  watch: {
    value(newVal, oldVal) {
      console.log(oldVal);
      console.log(newVal);
      this.$refs.mytable.hotInstance.loadData(oldVal);
    },
  },
};
</script>

<style src="../../node_modules/handsontable/dist/handsontable.full.css"></style>
