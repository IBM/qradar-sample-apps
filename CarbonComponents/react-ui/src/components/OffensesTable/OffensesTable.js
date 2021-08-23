/*
Copyright 2021 IBM Corporation
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

import { DataTablePagination } from '@carbon/ibm-security';
import './OffensesTable.scss';

const OffensesTable = ({ offenses }) => {
    const headers = [
        {
            key: 'magnitude',
            header: 'Magnitude',
        }, {
            key: 'offenseID',
            header: 'ID',
        }, {
            key: 'description',
            header: 'Description',
        }, {
            key: 'starttime',
            header: 'Start Time',
        }, {
            key: 'status',
            header: 'Status',
        },
    ];

    return (
        <div className="offenses-table-container">
            <DataTablePagination
                className="offenses-table"
                headers={headers}
                pageSize={10}
                pageSizes={[5, 10, 25, 50]}
                rows={offenses}
                isSelectable={false}
            />
        </div>
    );
}

export default OffensesTable;
