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
