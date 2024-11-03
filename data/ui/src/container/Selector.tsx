import WorldMap from "@/components/WorldMap"
import { useState } from "react";

export const Selector = () => {
    const [showMap, setShowMap] = useState(false);
    const [resetSegmentHandler, setResetSegmentHandler] = useState(false);
    const [exportData, setExportData] = useState(false);

    const [width, setWidth] = useState<number>(0);
    const [height, setHeight] = useState<number>(0);

    const [mapWidth, setMapWidth] = useState<number>(0);
    const [mapHeight, setMapHeight] = useState<number>(0);

    const generateMapHandler = () => {
        setMapWidth(width);
        setMapHeight(height);
        setShowMap(true);
    }

    return (
        <div style={{border: '2px solid grey', borderRadius: '5px', width: 'fill', background: '#fffff', padding: '15px', display: 'flex', flexDirection: 'column', gap: '15px'}}>
            <h2 style={{color: 'black', }}>Map Settings</h2>
            <hr/>
            <div style={{display: 'flex', flexDirection: 'row', gap: '10px'}}>
                <input
                    style={{
                        width: '250px',
                        padding: '0.75rem 1rem',
                        fontSize: '1rem',
                        lineHeight: '1.5',
                        color: '#374151',
                        backgroundColor: '#ffffff',
                        border: '2px solid #b5b5b7',
                        borderRadius: '0.375rem',
                        outline: 'none',
                        transition: 'border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out'
                    }}
                    type="number"
                    min={0}
                    placeholder="Segment Width (Degrees)"
                    onFocus={(e) => {
                        e.target.style.borderColor = '#3b82f6';
                        e.target.style.boxShadow = '0 0 0 3px rgba(59, 130, 246, 0.1)';
                    }}
                    onBlur={(e) => {
                        e.target.style.borderColor = '#e5e7eb';
                        e.target.style.boxShadow = 'none';
                    }}
                    onChange={(e) => {
                        setShowMap(false);
                        setWidth(Number(e.target.value))
                    }}
                    />
                    
                <input
                    style={{
                        width: '250px',
                        padding: '0.75rem 1rem',
                        fontSize: '1rem',
                        lineHeight: '1.5',
                        color: '#374151',
                        backgroundColor: '#ffffff',
                        border: '2px solid #b5b5b7',
                        borderRadius: '0.375rem',
                        outline: 'none',
                        transition: 'border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out'
                    }}
                    type="number"
                    min={0}
                    placeholder="Segment Height (Degrees)"
                    onFocus={(e) => {
                        e.target.style.borderColor = '#3b82f6';
                        e.target.style.boxShadow = '0 0 0 3px rgba(59, 130, 246, 0.1)';
                    }}
                    onBlur={(e) => {
                        e.target.style.borderColor = '#e5e7eb';
                        e.target.style.boxShadow = 'none';
                    }}
                    onChange={(e) => {
                        setShowMap(false);
                        setHeight(Number(e.target.value))
                    }}
                    />
                    <button
                    style={{
                        padding: '0.75rem 1.5rem',
                        backgroundColor: '#3b82f6',
                        color: '#ffffff',
                        border: 'none',
                        borderRadius: '0.375rem',
                        fontSize: '1rem',
                        fontWeight: '500',
                        cursor: 'pointer',
                        transition: 'all 0.2s ease',
                        display: 'inline-flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        boxShadow: '0 1px 2px rgba(0, 0, 0, 0.05)'
                    }}
                    onMouseOver={(e) => {
                        e.target.style.backgroundColor = '#2563eb';
                        e.target.style.transform = 'translateY(-1px)';
                    }}
                    onMouseLeave={(e) => {
                        e.target.style.backgroundColor = '#3b82f6';
                        e.target.style.transform = 'translateY(0)';
                    }}
                    onMouseDown={(e) => {
                        e.target.style.transform = 'translateY(0)';
                    }}
                    onClick={generateMapHandler}
                    type="submit"
                    >
                    Generate
                    </button>

                    <button
                    style={{
                        padding: '0.75rem 1.5rem',
                        backgroundColor: '#6B7280',
                        color: '#ffffff',
                        border: 'none',
                        borderRadius: '0.375rem',
                        fontSize: '1rem',
                        fontWeight: '500',
                        cursor: 'pointer',
                        transition: 'all 0.2s ease',
                        display: 'inline-flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        boxShadow: '0 1px 2px rgba(0, 0, 0, 0.05)'
                    }}
                    onMouseOver={(e) => {
                        e.target.style.backgroundColor = '#4B5563';
                        e.target.style.transform = 'translateY(-1px)';
                    }}
                    onMouseLeave={(e) => {
                        e.target.style.backgroundColor = '#6B7280';
                        e.target.style.transform = 'translateY(0)';
                    }}
                    onMouseDown={(e) => {
                        e.target.style.transform = 'translateY(0)';
                    }}
                    onClick={() => { setResetSegmentHandler(!resetSegmentHandler)}}
                    type="submit"
                    >
                    Reset
                    </button>

                    <button
                    style={{
                        padding: '0.75rem 1.5rem',
                        backgroundColor: '#25a536',
                        color: '#ffffff',
                        border: 'none',
                        borderRadius: '0.375rem',
                        fontSize: '1rem',
                        fontWeight: '500',
                        cursor: 'pointer',
                        transition: 'all 0.2s ease',
                        display: 'inline-flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        boxShadow: '0 1px 2px rgba(0, 0, 0, 0.05)'
                    }}
                    onMouseOver={(e) => {
                        e.target.style.backgroundColor = '#196f24';
                        e.target.style.transform = 'translateY(-1px)';
                    }}
                    onMouseLeave={(e) => {
                        e.target.style.backgroundColor = '#25a536';
                        e.target.style.transform = 'translateY(0)';
                    }}
                    onMouseDown={(e) => {
                        e.target.style.transform = 'translateY(0)';
                    }}
                    onClick={() => { setExportData(!exportData)}}
                    type="submit"
                    >
                    Export
                    </button>
                    
                </div>
                { showMap && (
                <div style={{display: 'flex', flexDirection: 'column', gap: '15px'}}>
                <hr/>
                
                
                <WorldMap width={mapWidth} height={mapHeight} reset={resetSegmentHandler} exportData={exportData} />
                </div>
                )}
            </div>
            
    )
}