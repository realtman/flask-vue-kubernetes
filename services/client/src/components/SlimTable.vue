<template>
    <slim-grid :data="data" :show-pager="false" :column-ptions="columnOptions"></slim-grid>
</template>

<script>
import SlimGrid from 'vue-slimgrid';

export default {
  components: { SlimGrid },
  props: ['colnames'],
  data() {
    return {
      data: this.initializeData(this.colnames),
      columnOptions: {
        editable: true,
        enableAddRow: true,
        enableCellNavigation: true,
        asyncEditorLoading: false,
        autoEdit: false,
        autoHeight: true
      },
    };
  },
  methods: {
    initializeData(colnames) {
      const row = { id: 0 };
      const data = [];
      for (let i = 0; i < colnames.length; i += 1) {
        row[colnames[i]] = '';
      }
      data.push(row);
      return data;
    },
  },
};
</script>

<style src="../../node_modules/vue-slimgrid/dist/slimgrid.css"></style>
