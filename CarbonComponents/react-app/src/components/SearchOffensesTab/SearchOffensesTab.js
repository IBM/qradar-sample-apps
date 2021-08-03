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
import { Button, CodeSnippet, Loading, Search, TitleBarModule } from '@carbon/ibm-security';
import useLazyFetch from '../../hooks/useLazyFetch';
import './SearchOffensesTab.scss'

const SearchOffensesTab = () => {
    const [searchID, setSearchID] = useState('');
    const [isInvalidID, setInvalidID] = useState(false);
    const [fetchData, { data, loading }] = useLazyFetch(`/offenses/${searchID}`);
    const [offense, setOffense] = useState();

    useEffect(() => {
        if (data?.offense) {
            setOffense(data.offense);
        }
    }, [data]);

    const onSearchBarChange = (event) => {
        setSearchID(event.target.value);
        validateSearchText(event.target.value);
    };

    const onSearchBarSubmit = async() => {
        fetchData();
    };

    const onSearchBarKeyDown = (event) => {
        if(event.key === 'Enter') {
            onSearchBarSubmit();
        }
    };

    const validateSearchText = (text) => {
        if (!text.match(/^[0-9]+$/)) {
            setInvalidID(true);
        } else {
            setInvalidID(false);
        }
    };

    const shouldDisableButton = () => {
        if (searchID === '' || isInvalidID) {
            return true;
        }

        return false;
    }

    return (
        <>
            {loading && <Loading />}
            <TitleBarModule title="Search offenses" />
            <p>Use the search bar below to fetch an offense by its ID.</p>
            <div className="offenses-searchbar">
                <div className="offenses-searchbar-inner">
                    <Search
                        className={isInvalidID ? 'searchbar-invalid' : ''}
                        clearButtonLabelText="Clear"
                        labelText="Label"
                        onChange={onSearchBarChange}
                        onKeyDown={onSearchBarKeyDown}
                        placeHolderText="Enter an offense ID"
                        submitLabel="Search"
                        value={searchID}
                    />
                    {isInvalidID && <span className="searchbar-invalid-msg">Offense IDs should contain numerical characters only.</span>}
                </div>
                <Button onClick={onSearchBarSubmit} disabled={shouldDisableButton()}>Search</Button>
            </div>
            {offense &&
            <>
                <h5>Result</h5>
                <CodeSnippet
                    showLessText="Show less"
                    showMoreText="Show more"
                    type="multi"
                    wrapText={false}
                >
                    <div>
                        <pre>
                            {JSON.stringify(offense, null, 2)}
                        </pre>
                    </div>
                </CodeSnippet>
                </>
            }
        </>
    );
}

export default SearchOffensesTab;
