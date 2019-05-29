<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Model Parameters</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm"
                v-b-modal.model-modal>Add Model</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Model Label</th>
              <th scope="col">Starting Inventory (Bushels)</th>
              <th scope="col">Selling Price ($/Bushel)</th>
              <th scope="col">Shortage Cost ($/Bushel)</th>
              <th scope="col">Salvage Value ($/Bushel)</th>
              <th scope="col">NA Production Cost ($/Acre)</th>
              <th scope="col">NA Processing Cost ($/(Bushel*Acre))</th>
              <th scope="col">SA Production Cost ($/Acre)</th>
              <th scope="col">SA Processing Cost ($/(Bushel*Acre))</th>
              <th scope="col">Expected NA Yield (Bushels/Acre)</th>
              <th scope="col">Expected SA Yield (Bushels/Acre)</th>
              <th scope="col">Expected Demand (Bushels)</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(model, index) in models" :key="index">
              <td>{{ model.label }}</td>
              <td>{{ model.starting_inventory }}</td>
              <td>{{ model.price }}</td>
              <td>{{ model.shortage }}</td>
              <td>{{ model.salvage }}</td>
              <td>{{ model.production_na }}</td>
              <td>{{ model.processing_na }}</td>
              <td>{{ model.production_sa }}</td>
              <td>{{ model.processing_sa }}</td>
              <td>{{ model.yield_na }}</td>
              <td>{{ model.yield_sa }}</td>
              <td>{{ model.demand }}</td>
              <td>
                <button type="button"
                        class="btn btn-warning btn-sm"
                        style="padding-bottom:5px"
                        v-b-modal.model-update-modal
                        @click="editModel(model)">
                  Update
                </button>
                <button type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteModel(model)">
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addmodelModal"
             id="model-modal"
             size="huge"
             title="Add a new model"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-container fluid>
          <b-form-group id="form-label">
            <label for="form-label-input">
              Model Label (<i>optional</i>):
            </label>
            <b-form-input id="form-label-input"
                          type="text"
                          v-model="addmodelForm.label"
                          placeholder="Enter label for model">
            </b-form-input>
          </b-form-group>
          <b-form-row id="form-starting_inventory-price">
            <b-col id="form-starting_inventory" cols="6">
              <label for="form-starting_inventory-input">
                Starting Inventory (Bushels):
              </label>
              <b-form-input id="form-starting_inventory-input"
                            type="text"
                            v-model="addmodelForm.starting_inventory"
                            required
                            placeholder="Enter starting inventory">
              </b-form-input>
            </b-col>
            <b-col id="form-price" cols="6">
              <label for="form-price-input">
                Selling Price ($/Bushel):
              </label>
              <b-form-input id="form-price-input"
                            type="text"
                            v-model="addmodelForm.price"
                            required
                            placeholder="Enter price">
              </b-form-input>
            </b-col>
          </b-form-row>

          <b-form-row id="form-shortage-salvage" style="margin-top:10px">
            <b-col id="form-shortage" cols="6">
              <label for="form-shortage-input">
                Shortage Cost ($/Bushel):
              </label>
              <b-form-input id="form-shortage-input"
                            type="text"
                            v-model="addmodelForm.shortage"
                            required
                            placeholder="Enter shortage cost">
              </b-form-input>
            </b-col>
            <b-col id="form-salvage" cols="6">
              <label for="form-salvage-input">
                Salvage Value ($/Bushel):
              </label>
              <b-form-input id="form-salvage-input"
                            type="text"
                            v-model="addmodelForm.salvage"
                            required
                            placeholder="Enter salvage value">
              </b-form-input>
            </b-col>
          </b-form-row>

          <b-form-row id="form-production_na-processing_na" style="margin-top:10px">
            <b-col id="form-production_na" cols="6">
              <label for="form-production_na-input">
                NA Production Cost ($/Acre):
              </label>
              <b-form-input id="form-production_na-input"
                            type="text"
                            v-model="addmodelForm.production_na"
                            required
                            placeholder="Enter NA production cost">
              </b-form-input>
            </b-col>
            <b-col id="form-processing_na" cols="6">
              <label for="form-processing_na-input">
                NA Processing Cost ($/(Bushel*Acre)):
              </label>
              <b-form-input id="form-processing_na-input"
                            type="text"
                            v-model="addmodelForm.processing_na"
                            required
                            placeholder="Enter NA processing cost">
              </b-form-input>
            </b-col>
          </b-form-row>

          <b-form-row id="form-production_sa-processing_sa" style="margin-top:10px">
            <b-col id="form-production_sa" cols="6">
              <label for="form-production_sa-input">
                SA Production Cost ($/Acre):
              </label>
              <b-form-input id="form-production_sa-input"
                            type="text"
                            v-model="addmodelForm.production_sa"
                            required
                            placeholder="Enter SA production cost">
              </b-form-input>
            </b-col>
            <b-col id="form-processing_sa" cols="6">
              <label for="form-processing_sa-input">
                SA Processing Cost ($/(Bushel*Acre)):
              </label>
              <b-form-input id="form-processing_sa-input"
                            type="text"
                            v-model="addmodelForm.processing_sa"
                            required
                            placeholder="Enter SA processing cost">
              </b-form-input>
            </b-col>
          </b-form-row>

          <b-form-row id="form-tables" style="margin-top:30px;margin-bottom:30px">
            <b-col id="form-yield_na" cols="3">
              <div style="width:100%">
                <sheet :colnames="['NA Yield Probability','NA Yield (Bushels/Acre)']"
                        @onChangeSheet="addmodelForm.yield_na = $event"></sheet>
              </div>
            </b-col>
            <b-col id="form-yield_sa" cols="3">
              <div style="width:100%">
                <sheet :colnames="['SA Yield Probability','SA Yield (Bushels/Acre)']"
                       @onChangeSheet="addmodelForm.yield_sa = $event"></sheet>
              </div>
            </b-col>
            <b-col id="form-demand" cols="3">
              <div style="width:100%">
                <sheet :colnames="['Demand Probability','Demand (Bushels)']"
                       @onChangeSheet="addmodelForm.demand = $event"></sheet>
              </div>
            </b-col>
          </b-form-row>
        </b-container>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editModelModal"
             id="model-update-modal"
             size="huge"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-container fluid>
          <b-form-group id="form-edit-label">
            <label for="form-edit-label-input">
              Model Label (<i>optional</i>):
            </label>
            <b-form-input id="form-edit-label-input"
                          type="text"
                          v-model="editForm.label"
                          placeholder="Enter label for model">
            </b-form-input>
          </b-form-group>
          <b-form-row id="form-edit-starting_inventory-price">
            <b-col id="form-edit-starting_inventory" cols="6">
              <label for="form-edit-starting_inventory-input">
                Starting Inventory (Bushels):
              </label>
              <b-form-input id="form-edit-starting_inventory-input"
                            type="text"
                            v-model="editForm.starting_inventory"
                            required
                            placeholder="Enter starting inventory">
              </b-form-input>
            </b-col>
            <b-col id="form-edit-price" cols="6">
              <label for="form-edit-price-input">
                Selling Price ($/Bushel):
              </label>
              <b-form-input id="form-edit-price-input"
                            type="text"
                            v-model="editForm.price"
                            required
                            placeholder="Enter price">
              </b-form-input>
            </b-col>
          </b-form-row>

          <b-form-row id="form-edit-shortage-salvage" style="margin-top:10px">
            <b-col id="form-edit-shortage" cols="6">
              <label for="form-edit-shortage-input">
                Shortage Cost ($/Bushel):
              </label>
              <b-form-input id="form-edit-shortage-input"
                            type="text"
                            v-model="editForm.shortage"
                            required
                            placeholder="Enter shortage cost">
              </b-form-input>
            </b-col>
            <b-col id="form-edit-salvage" cols="6">
              <label for="form-edit-salvage-input">
                Salvage Value ($/Bushel):
              </label>
              <b-form-input id="form-edit-salvage-input"
                            type="text"
                            v-model="editForm.salvage"
                            required
                            placeholder="Enter salvage value">
              </b-form-input>
            </b-col>
          </b-form-row>

          <b-form-row id="form-edit-production_na-processing_na" style="margin-top:10px">
            <b-col id="form-edit-production_na" cols="6">
              <label for="form-edit-production_na-input">
                NA Production Cost ($/Acre):
              </label>
              <b-form-input id="form-edit-production_na-input"
                            type="text"
                            v-model="editForm.production_na"
                            required
                            placeholder="Enter NA production cost">
              </b-form-input>
            </b-col>
            <b-col id="form-edit-processing_na" cols="6">
              <label for="form-edit-processing_na-input">
                NA Processing Cost ($/(Bushel*Acre)):
              </label>
              <b-form-input id="form-edit-processing_na-input"
                            type="text"
                            v-model="editForm.processing_na"
                            required
                            placeholder="Enter NA processing cost">
              </b-form-input>
            </b-col>
          </b-form-row>

          <b-form-row id="form-edit-production_sa-processing_sa" style="margin-top:10px">
            <b-col id="form-edit-production_sa" cols="6">
              <label for="form-edit-production_sa-input">
                SA Production Cost ($/Acre):
              </label>
              <b-form-input id="form-edit-production_sa-input"
                            type="text"
                            v-model="editForm.production_sa"
                            required
                            placeholder="Enter SA production cost">
              </b-form-input>
            </b-col>
            <b-col id="form-edit-processing_sa" cols="6">
              <label for="form-edit-processing_sa-input">
                SA Processing Cost ($/(Bushel*Acre)):
              </label>
              <b-form-input id="form-edit-processing_sa-input"
                            type="text"
                            v-model="editForm.processing_sa"
                            required
                            placeholder="Enter SA processing cost">
              </b-form-input>
            </b-col>
          </b-form-row>

          <b-form-row id="form-edit-tables" style="margin-top:30px;margin-bottom:30px">
            <b-col id="form-edit-yield_na" cols="3">
              <div style="width:100%">
                <sheet :colnames="['NA Yield Probability','NA Yield (Bushels/Acre)']"
                       :value="editForm.yield_na"
                       @onChangeSheet="editForm.yield_na = $event"></sheet>
              </div>
            </b-col>
            <b-col id="form-edit-yield_sa" cols="3">
              <div style="width:100%">
                <sheet :colnames="['SA Yield Probability','SA Yield (Bushels/Acre)']"
                       v-model="editForm.yield_sa"
                       @onChangeSheet="editForm.yield_sa = $event"></sheet>
              </div>
            </b-col>
            <b-col id="form-edit-demand" cols="3">
              <div style="width:100%">
                <sheet :colnames="['Demand Probability','Demand (Bushels)']"
                       v-model="editForm.demand = $event"
                       @onChangeSheet="editForm.demand = $event"></sheet>
              </div>
            </b-col>
          </b-form-row>
        </b-container>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from '../components/Alert';
import Sheet from '../components/Spreadsheet';

export default {
  data() {
    return {
      models: [],
      addmodelForm: {
        label: null,
        starting_inventory: null,
        price: null,
        shortage: null,
        salvage: null,
        production_na: null,
        processing_na: null,
        production_sa: null,
        processing_sa: null,
        yield_na: [],
        yield_sa: [],
        demand: [],
      },
      editForm: {
        id: null,
        label: null,
        starting_inventory: null,
        price: null,
        shortage: null,
        salvage: null,
        production_na: null,
        processing_na: null,
        production_sa: null,
        processing_sa: null,
        yield_na: [],
        yield_sa: [],
        demand: [],
      },
      message: '',
      showMessage: false,
      ROOT_API: process.env.ROOT_API,
    };
  },
  components: {
    alert: Alert,
    sheet: Sheet,
  },
  methods: {
    getmodels() {
      const path = `${this.ROOT_API}/models`;
      axios.get(path)
        .then((res) => {
          this.models = res.data.models;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addmodel(payload) {
      const path = `${this.ROOT_API}/models`;
      axios.post(path, payload)
        .then(() => {
          this.getmodels();
          this.message = 'Model added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getmodels();
        });
    },
    updatemodel(payload, modelID) {
      const path = `${this.ROOT_API}/models/${modelID}`;
      axios.put(path, payload)
        .then(() => {
          this.getmodels();
          this.message = 'Model updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getmodels();
        });
    },
    removemodel(modelID) {
      const path = `${this.ROOT_API}/models/${modelID}`;
      axios.delete(path)
        .then(() => {
          this.getmodels();
          this.message = 'Model removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getmodels();
        });
    },
    initForm() {
      Object.keys(this.addmodelForm).forEach((key) => {
        if ((key in ['yield_na', 'yield_sa', 'demand'])) {
          this.addmodelForm[key] = [];
        } else {
          this.addmodelForm[key] = null;
        }
      });
      Object.keys(this.editForm).forEach((key) => {
        if ((key in ['yield_na', 'yield_sa', 'demand'])) {
          this.editForm[key] = [];
        } else {
          this.editForm[key] = null;
        }
      });
      // this.addmodelForm.starting_inventory = '';
      // this.addmodelForm.price = '';
      // this.addmodelForm.shortage = '';
      // this.addmodelForm.salvage = '';
      // this.addmodelForm.production_na = '';
      // this.addmodelForm.processing_na = '';
      // this.addmodelForm.production_sa = '';
      // this.addmodelForm.processing_sa = '';
      // this.addmodelForm.yield_prob_na = [];
      // this.addmodelForm.yield_na = [];
      // this.addmodelForm.yield_sa = [];
      // this.addmodelForm.demand = [];
      // this.editForm.id = '';
      // this.editForm.starting_inventory = '';
      // this.editForm.price = '';
      // this.editForm.shortage = '';
      // this.editForm.salvage = '';
      // this.editForm.production_na = '';
      // this.editForm.processing_na = '';
      // this.editForm.production_sa = '';
      // this.editForm.processing_sa = '';
      // this.editForm.yield_prob_na = [];
      // this.editForm.yield_na = [];
      // this.editForm.yield_prob_sa = [];
      // this.editForm.yield_sa = [];
      // this.editForm.demand_prob = [];
      // this.editForm.demand = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addmodelModal.hide();
      const payload = {};
      Object.entries(this.addmodelForm).forEach(([key, value]) => {
        payload[key] = value;
      });
      this.addmodel(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editModelModal.hide();
      const payload = {};
      Object.entries(this.editForm).forEach(([key, value]) => {
        payload[key] = value;
      });
      this.updatemodel(payload, this.editForm.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addmodelModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editModelModal.hide();
      this.initForm();
      this.getmodels(); // why?
    },
    onDeleteModel(model) {
      this.removemodel(model.id);
    },
    editModel(model) {
      this.editForm = model;
    },
  },
  created() {
    this.getmodels();
  },
};
</script>

<style>
.modal .modal-huge {
  max-width: 1300px;
  width: 1300px;
}
</style>
<style src="../../node_modules/handsontable/dist/handsontable.full.css"></style>
