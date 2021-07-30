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
