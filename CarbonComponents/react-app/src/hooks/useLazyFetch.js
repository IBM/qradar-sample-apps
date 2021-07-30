import { useState } from 'react';
import axios from 'axios';

const getBaseURL = (url) => {
    return url.substr(0, url.lastIndexOf('/'));
};

const useLazyFetch = (url, baseURL = window.location.href) => {
    const [data, setData] = useState();
    const [loading, setLoading] = useState(false);

    const fetchData = async() => {
        setLoading(true);
        setData();
        try {
            const { data } = await axios({
                method: 'GET',
                url,
                baseURL: getBaseURL(baseURL),
            });
            setData(data);
            setLoading(false);
        } catch (e) {
            console.error(e);
            setLoading(false);
        }
    };

    return [fetchData, { data, loading }];
};

export default useLazyFetch;
