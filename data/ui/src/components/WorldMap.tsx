import React, { useState, useMemo } from 'react';
import dynamic from 'next/dynamic';

const Plot = dynamic(() => import('react-plotly.js'), {
  ssr: false,
  loading: () => <div style={{color: 'orange'}}>Loading map...</div>
});

interface MapSegment {
  id: string;
  lon: number[];
  lat: number[];
  selected: boolean;
}

const WorldMap = () => {
  const [selectedSegments, setSelectedSegments] = useState<Set<string>>(new Set());

  const segments = useMemo(() => {
    const segs: MapSegment[] = [];
    for (let i = 90; i > -90; i -= 6) {
      for (let j = -180; j < 180; j += 6) {
        segs.push({
          id: `${i},${j}`,
          lon: [j, j + 6, j + 6, j, j],
          lat: [i, i, i - 6, i - 6, i],
          selected: false
        });
      }
    }
    return segs;
  }, []);

  const generateMapData = () => {
    return segments.map((segment) => ({
      type: 'scattergeo' as const,
      lon: segment.lon,
      lat: segment.lat,
      mode: 'lines+markers',
      fill: 'toself',
      line: {
        color: 'black',
        width: 1,
      },
      fillcolor: selectedSegments.has(segment.id) ? 'rgb(100, 149, 237)' : 'rgb(255, 255, 255)',
      opacity: selectedSegments.has(segment.id) ? 0.8 : 0.5,
      hoverinfo: 'text',
      text: `Grid: ${segment.id}`,
      customdata: [segment.id],
    }));
  };

  const layout = {
    title: {
        automargin: true,
        text: 'Segmented Map',
        pad: {
            b: -1000,
            t: 300
        },
        font: {
            size: 30
        },
    },
    width: 1500,
    height: 1500,
    margin: { l: 0, r: 0, b: 0, t: -1000 },
    padding: { l: 0, r: 0, b: 0, t: -1000 },
    geo: {
      resolution: 50,
      projection: {
        type: 'equirectangular',
      },
      showland: true,
      showcountries: true,
      showocean: true,
      bounds: {
        west: -180,
        east: 180,
        south: -66,
        north: 90,
      },
    },
    yaxis:{
        fixedrange: true
    },
    xaxis: {
        fixedrange: true
    },
    dragMode: false,
    showlegend: false,
  };

  const handleClick = (event: any) => {
    if (event.points && event.points[0]) {
      const segmentId = event.points[0].data.customdata[0];
      setSelectedSegments((prev) => {
        const newSelected = new Set(prev);
        if (newSelected.has(segmentId)) {
          newSelected.delete(segmentId);
        } else {
          newSelected.add(segmentId);
        }
        return newSelected;
      });
    }
  };

  return (
    <div>
      <div>
        <Plot
          data={generateMapData()}
          layout={layout}
          style={{  }}
          useResizeHandler={true}
          config={{ responsive: true, scrollZoom: false, displayModeBar: false }}
          onClick={handleClick}
        />
      </div>
     
    </div>
  );
};

export default WorldMap;