import axios from 'axios';

function getBaseURL(url) {
    return url.substr(0, url.lastIndexOf('/'));
}

export async function get(route, baseURL) {
    try {
        const { data } = await axios({
          url: route,
          baseURL: getBaseURL(baseURL),
        });
        return data;
    } catch (e) {
      console.error(e);
      return undefined;
    }
};
