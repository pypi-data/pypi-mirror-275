<!-- Copyright 2022 Karlsruhe Institute of Technology
   -
   - Licensed under the Apache License, Version 2.0 (the "License");
   - you may not use this file except in compliance with the License.
   - You may obtain a copy of the License at
   -
   -     http://www.apache.org/licenses/LICENSE-2.0
   -
   - Unless required by applicable law or agreed to in writing, software
   - distributed under the License is distributed on an "AS IS" BASIS,
   - WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   - See the License for the specific language governing permissions and
   - limitations under the License. -->

<template>
  <div class="input-group" @pointerdown.stop>
    <input v-model="value" class="form-control input" :title="value">
    <div class="input-group-append">
      <button type="button" class="btn btn-light" title="Revert to default" @click="value = defaultFormat">
        <i class="fa-solid fa-rotate"></i>
      </button>
    </div>
  </div>
</template>

<style scoped>
.input {
  width: 160px;
}
</style>

<script>
import workflowControlMixn from 'scripts/components/mixins/workflow-control-mixin';

export default {
  mixins: [workflowControlMixn],
  props: {
    defaultValue: String,
  },
  data() {
    return {
      defaultFormat: '',
    };
  },
  methods: {
    updateDefaultFormat(defaultFormat) {
      this.defaultFormat = defaultFormat;
    },
  },
};
</script>
