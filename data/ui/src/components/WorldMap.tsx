import React, { useState, useMemo, useEffect } from 'react';
import dynamic from 'next/dynamic';

const Plot = dynamic(() => import('react-plotly.js'), {
  ssr: false,
  // loading: () => <div style={{color: 'orange'}}>Loading map...</div>
});

const URL = 'http://localhost:5000'
interface MapSegment {
  id: string;
  lon: number[];
  lat: number[];
  selected: boolean;
}

const WorldMap = ({width, height, reset, exportData}: {width: number, height: number, reset: boolean, exportData: boolean}) => {
  const [selectedSegments, setSelectedSegments] = useState<Set<string>>(new Set());
  
  const exportSegmentData = async () => {
    try {
      const response = await fetch(`${URL}/api/export`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
      });

      if (response.ok) {

      }

    } catch (err) {
      console.log(err)
    }
  }
  useEffect(() => {
    setSelectedSegments(new Set())
  }, [reset])

  useEffect(() => {
    exportSegmentData()
  }, [exportData])
  const segments = useMemo(() => {
    const segs: MapSegment[] = [];
    for (let i = 90; i > -90; i -= height) {
      for (let j = -180; j < 180; j += width) {
        segs.push({
          id: `${i},${j}`,
          lon: [j, j + width, j + width, j, j],
          lat: [i, i, i - height, i - height, i],
          selected: false
        });
      }
    }
    return segs;
  }, [width, height]);

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
    // title: {
    //     automargin: true,
    //     text: 'Segmented Map',
    //     pad: {
    //         b: 0,
    //         t: 0
    //     },
    //     font: {
    //         size: 30
    //     },
    // },
    autosize: true,
    // width: 1500,
    height: 750,
    margin: { l: 0, r: 0, b: 0, t: 0 },
    padding: { l: 0, r: 0, b: 0, t: 0 },
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
    <div style={{display: 'flex', flexDirection: 'row'}}>
      <div style={{ width: '75%', height: '850px', borderRight: '1px solid black', padding: '50px 0 50px 0'}}>
        <Plot
          data={generateMapData()}
          layout={layout}
          style={{  }}
          useResizeHandler={true}
          config={{ responsive: true, scrollZoom: false, displayModeBar: false }}
          onClick={handleClick}
        />
      </div>

      <div>
        <ul style={{padding: '50px', display: 'flex', flexDirection: 'column', flexWrap: 'wrap', height: '850px'}}>
            {Array.from(selectedSegments).map((segment, i) => 
                <li key={i} style={{fontSize: 30, color: 'black', marginRight: '35px'}}>{segment}</li>
            )}
        </ul>
      </div>
     
    </div>
  );
};

export default WorldMap;