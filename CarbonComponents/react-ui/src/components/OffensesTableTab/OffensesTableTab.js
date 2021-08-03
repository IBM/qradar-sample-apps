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
