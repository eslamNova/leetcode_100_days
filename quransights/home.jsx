import React, { useState, useEffect, lazy, Suspense } from 'react';
import { Moon, Github, MessageCircle } from 'lucide-react';
import ramadanData from './data.json';

const DayModal = lazy(() => import('./components/DayModal'));

interface DayData {
  title: string;
  content: string;
}

function App() {
  const [selectedDay, setSelectedDay] = useState<number | null>(null);
  const [dayData, setDayData] = useState<DayData | null>(null);
  const [readDays, setReadDays] = useState<number[]>([]);

  useEffect(() => {
    if (selectedDay) {
      setDayData(ramadanData.days[selectedDay as keyof typeof ramadanData.days]);
    }
  }, [selectedDay]);

  useEffect(() => {
    const savedReadDays = localStorage.getItem('readDays');
    if (savedReadDays) {
      setReadDays(JSON.parse(savedReadDays));
    }
  }, []);

  const handleDayClick = (day: number) => {
    setSelectedDay(day);
  };

  const closeModal = () => {
    setSelectedDay(null);
    setDayData(null);
  };

  const handleMarkAsRead = (day: number) => {
    const newReadDays = readDays.includes(day) 
      ? readDays.filter(d => d !== day) 
      : [...readDays, day];
    
    setReadDays(newReadDays);
    localStorage.setItem('readDays', JSON.stringify(newReadDays));
  };

  // Sample Quran chapters for demonstration
  const quranChapters = [
    "البقرة", "آل عمران", "النساء", "المائدة", "الأنعام",
    "الأعراف", "الأنفال", "التوبة", "يونس", "هود"
  ];

  const calculatePosition = (index: number, total: number, radius: number) => {
    const angle = ((index / total) * 2 * Math.PI) - (Math.PI / 2); // Start from top
    return {
      x: 50 + radius * Math.cos(angle),
      y: 50 + radius * Math.sin(angle)
    };
  };

  return (
    <div className="min-h-screen">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <header className="text-center mb-12">
          <div className="w-40 h-40 mx-auto bg-white rounded-full shadow-lg flex items-center justify-center mb-6 floating">
            <Moon className="w-20 h-20 text-primary" />
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-primary mb-4">دروس الشيخ ماجد</h1>
          <p className="text-lg text-accent mb-2">مسجد الهدى - رمضان 1446</p>
          <a
            href="https://t.me/engafr"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center text-primary hover:text-accent transition-colors"
          >
            <MessageCircle className="w-5 h-5 ml-2" />
            قناة الشيخ ماجد على تليجرام
          </a>
        </header>

        {/* Calendar Grid */}
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-12">
          {Array.from({ length: 30 }, (_, i) => i + 1).map((day) => (
            <div
              key={day}
              className={`day-cell ${selectedDay === day ? 'active' : ''} ${
                readDays.includes(day) ? 'bg-green-100 hover:bg-green-200' : ''
              }`}
              onClick={() => handleDayClick(day)}
            >
              <div className="text-center">
                <span className="text-2xl font-bold text-primary">{day}</span>
                <h3 className="text-sm text-accent mt-2">
                  {ramadanData.days[day as keyof typeof ramadanData.days].title}
                </h3>
              </div>
            </div>
          ))}
        </div>

        {/* Footer */}
        <footer className="text-center text-primary mt-8">
          <p className="text-lg text-accent mb-2">تم تدوين هذه النصوص مباشرةً أثناء الدروس وقمت بنشرها سريعًا قبل التدقيق وإكمال ما نقص للمراجعة السريعة قبل الامتحان، على أن يتم العمل على هذا الأمر بشكل محكم إن شاء الله، ولذا قد تجد بعض الأخطاء الإملائية أو الجمل غير المكتملة، ولا بأس فكان الهدف هو الإلمام بجل كلام الشيخ ماجد ومحاولة تحرير أهم النقاط قدر المستطاع. ولمن يرغب في المساهمة بالتدقيق و التنسيق فيما بعد إن شاء الله، يمكنه التواصل معي عبر واتساب  <a href="https://wa.me/201010698334" className="text-blue-500 underline">01010698334</a>.</p>
        </footer>

        {/* Divider */}
        <div className="relative py-16">
          <div className="absolute inset-0 flex items-center">
            <div className="w-full border-t border-gray-300"></div>
          </div>
          <div className="relative flex justify-center">
            <span className="bg-[#f8f4e9] px-4 text-2xl font-bold text-primary">
              روابط القرآن
            </span>
          </div>
        </div>

        {/* Quran Connections Section */}
        <div className="bg-gradient-to-br from-primary/5 to-secondary/5 rounded-2xl p-8 mb-12">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold text-primary mb-4">روابط وموضوعات القرآن الكريم</h2>
            <p className="text-accent text-lg">قيد التطوير - سيتم إضافة المحتوى قريباً إن شاء الله</p>
          </div>
          
          {/* 3D Connection Visualization */}
          <div className="connections-container">
            <div className="absolute inset-0 bg-[radial-gradient(#1a472a_1px,transparent_1px)] [background-size:20px_20px] opacity-20"></div>
            
            {/* Connection Lines with Arrows */}
            <svg className="absolute inset-0 w-full h-full" style={{ zIndex: 5 }}>
              <defs>
                <marker
                  id="arrowhead"
                  markerWidth="10"
                  markerHeight="7"
                  refX="9"
                  refY="3.5"
                  orient="auto"
                >
                  <polygon
                    points="0 0, 10 3.5, 0 7"
                    fill="rgba(26, 71, 42, 0.4)"
                  />
                </marker>
              </defs>
              {quranChapters.map((_, i) => {
                const connections = [
                  (i + 1) % quranChapters.length,
                  (i + 2) % quranChapters.length
                ];
                
                return connections.map(j => {
                  const pos1 = calculatePosition(i, quranChapters.length, 35);
                  const pos2 = calculatePosition(j, quranChapters.length, 35);
                  
                  return (
                    <path
                      key={`${i}-${j}`}
                      d={`M ${pos1.x}% ${pos1.y}% Q 50% 50% ${pos2.x}% ${pos2.y}%`}
                      fill="none"
                      stroke="rgba(26, 71, 42, 0.2)"
                      strokeWidth="2"
                      className="connection-arrow"
                      markerEnd="url(#arrowhead)"
                    />
                  );
                });
              })}
            </svg>

            {/* Chapter Nodes */}
            {quranChapters.map((chapter, index) => {
              const position = calculatePosition(index, quranChapters.length, 35);
              
              return (
                <div
                  key={chapter}
                  className="quran-node absolute transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-full p-4 shadow-lg hover:shadow-xl transition-all duration-300 cursor-pointer hover:scale-110"
                  style={{
                    left: `${position.x}%`,
                    top: `${position.y}%`,
                    zIndex: 10,
                    '--delay': `${index * 0.2}s`
                  } as React.CSSProperties}
                >
                  <span className="text-primary font-bold whitespace-nowrap">{chapter}</span>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Day Modal */}
      {selectedDay && dayData && (
        <Suspense fallback={<div className="modal-overlay fixed inset-0 flex items-center justify-center">جاري التحميل...</div>}>
          <DayModal
            day={selectedDay}
            title={dayData.title}
            content={dayData.content}
            onClose={closeModal}
            isRead={readDays.includes(selectedDay)}
            onMarkAsRead={() => handleMarkAsRead(selectedDay)}
          />
        </Suspense>
      )}
    </div>
  );
}

export default App;