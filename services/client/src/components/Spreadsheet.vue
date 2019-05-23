<template>
    <hot-table v-bind:key="data.length" :data="data" :settings="hotSettings"></hot-table>
</template>

<script>
import { HotTable } from '@handsontable/vue';

export default {
  components: { HotTable },
  props: ['colnames'],
  data() {
    return {
      data: [['', '']],
      hotSettings: {
        colHeaders: this.colnames,
        rowHeaders: true,
        height: 320,
        licenseKey: 'non-commercial-and-evaluation',
      },
    };
  },
  // computed: {
  //   fieldModelValue: {
  //     get() {
  //       return this.value;
  //     },
  //     set(newValue) {
  //       this.$emit('input', newValue);
  //     },
  //   },
  // },
  methods: {
    // updateData() {
    //   console.log(JSON.stringify({ updateData: this.$refs.testHot.table.getSourceDataArray() }));
    //   this.$emit('input', this.$refs.testHot.table.getSourceDataArray());
    // },
  },
};
</script>

<style src="../../node_modules/handsontable/dist/handsontable.full.css"></style>
