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
      data: [['', '']],
      hotSettings: {
        colHeaders: this.colnames,
        rowHeaders: true,
        height: 320,
        licenseKey: 'non-commercial-and-evaluation',
      },
    };
  },
  methods: {
    setData(data) {
      this.$refs.hotTableComponent.hotInstance.loadData(data);
    },
  },
};
</script>

<style src="../../node_modules/handsontable/dist/handsontable.full.css"></style>
