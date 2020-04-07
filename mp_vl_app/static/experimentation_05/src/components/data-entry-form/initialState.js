import { materialRenderers, materialCells } from '@jsonforms/material-renderers';

export default {
    dataentryform: {
        init: false,
        isLoading: true,
        dataList: [],
    },
    jsonforms: {
        renderers: materialRenderers,
        cells: materialCells,
    }
}