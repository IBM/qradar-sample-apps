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

import React from 'react';
import { Tab, Tabs } from '@carbon/ibm-security';
import OffensesTableTab from './components/OffensesTableTab/OffensesTableTab';
import SearchOffensesTab from './components/SearchOffensesTab/SearchOffensesTab';
import './App.scss';

const App = () => (
    <div className="app">
        <h2>Sample application using Carbon components</h2>
        <Tabs>
            <Tab href="#" tabIndex={0} label="Offenses table">
                <OffensesTableTab />
            </Tab>
            <Tab href="#" tabIndex={1} label="Search offenses">
                <SearchOffensesTab />
            </Tab>
        </Tabs>
    </div>
);

export default App;
