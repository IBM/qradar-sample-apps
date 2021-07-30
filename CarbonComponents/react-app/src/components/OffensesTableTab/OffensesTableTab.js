import React, { useState, useEffect } from 'react';
import { Button, Loading, TitleBarModule } from '@carbon/ibm-security';
import { format } from 'date-fns';
import OffensesTable from '../OffensesTable/OffensesTable';
import useLazyFetch from '../../hooks/useLazyFetch';
import './OffensesTableTab.scss';

const OffensesTableTab = () => {
    const [fetchData, { data, loading }] = useLazyFetch(`/offenses?range=items=0-49`);
    const [offenses, setOffenses] = useState();

    useEffect(() => {
        const formatOffenses = (offenses) => {
            const formattedOffenses = offenses.map((offense) => {
                return {
                    id: offense.id,
                    magnitude: offense.magnitude,
                    offenseID: offense.id,
                    description: offense.description,
                    starttime: format(offense.start_time, 'MMM dd, yyyy  hh:mm a'),
                    status: offense.status,
                };
            });
            return formattedOffenses;
        };

        if (data?.offenses) {
            setOffenses(formatOffenses(data.offenses));
        }
    }, [data]);

    const getOffenses = async() => {
        fetchData();
    };

    const renderEmptyState = () => (
        <div className="offenses-empty-state">
            <TitleBarModule title="Offenses table" />
            <div className="empty-state-text">
                <p>This tab displays a list of offenses in a table.</p>
                <p>Click the button below to fetch the last 50 offenses.</p>
            </div>
            <Button onClick={() => getOffenses()}>Fetch offenses</Button>
        </div>
    );

    return (
        <>
            {loading && <Loading />}
            {!offenses?.length && renderEmptyState()}
            {offenses?.length &&
                <div className="offenses-tab-container">
                    <div>
                        <TitleBarModule title="Offenses table" />
                        <div className="offenses-text-button-pair">
                            <p>The {offenses?.length} most recent offenses are displayed in the table below.</p>
                            <div>
                                <Button onClick={() => setOffenses(undefined)} size="sm" kind="ghost">
                                    Clear table
                                </Button>
                                <Button onClick={() => getOffenses()} size="sm" kind="ghost">
                                    Refresh table
                                </Button>
                            </div>
                        </div>
                    </div> 
                    <OffensesTable offenses={offenses} />
                </div>
            }
        </>
    );
}

export default OffensesTableTab;
