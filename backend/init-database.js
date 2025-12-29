const fs = require('fs');
const path = require('path');

const DATA_DIR = path.join(__dirname, 'data');
const ARTICLES_FILE = path.join(DATA_DIR, 'articles.json');
const CONTACTS_FILE = path.join(DATA_DIR, 'contacts.json');
const ADMINS_FILE = path.join(DATA_DIR, 'admins.json');

console.log('');
console.log('========================================');
console.log('   KHOI TAO DATABASE JSON');
console.log('========================================');
console.log('');

// Tao thu muc data neu chua co
if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR);
    console.log('Da tao thu muc data/');
}

// Tao file articles.json
console.log('Dang tao file articles.json...');
const articles = {
    articles: [
        {
            id: 1,
            title: 'Luat Doanh nghiep 2020 - Nhung diem moi quan trong',
            content: 'Luat Doanh nghiep so 59/2020/QH14 co hieu luc tu ngay 01/01/2021, thay the Luat Doanh nghiep 2014.',
            created_at: '2025-01-15'
        },
        {
            id: 2,
            title: 'Quy dinh moi ve thue TNCN nam 2025',
            content: 'Muc giam tru gia canh cho nguoi nop thue la 11 trieu dong/thang va 4,4 trieu dong/thang cho moi nguoi phu thuoc.',
            created_at: '2025-01-14'
        },
        {
            id: 3,
            title: 'Huong dan dang ky BHXH cho doanh nghiep moi',
            content: 'Doanh nghiep moi thanh lap phai dang ky tham gia BHXH trong vong 30 ngay ke tu ngay ky hop dong lao dong dau tien.',
            created_at: '2025-01-13'
        }
    ]
};
fs.writeFileSync(ARTICLES_FILE, JSON.stringify(articles, null, 2));
console.log('   Da tao file articles.json voi 3 bai viet mau!');

// Tao file contacts.json
console.log('Dang tao file contacts.json...');
const contacts = {
    contacts: [
        {
            id: 1,
            name: 'Nguyen Van A',
            phone: '0901234567',
            email: 'nguyenvana@email.com',
            message: 'Toi muon duoc tu van ve thanh lap cong ty TNHH',
            created_at: '2025-01-15'
        }
    ]
};
fs.writeFileSync(CONTACTS_FILE, JSON.stringify(contacts, null, 2));
console.log('   Da tao file contacts.json voi 1 lien he mau!');

// Tao file admins.json
console.log('Dang tao file admins.json...');
const admins = {
    admins: [
        {
            id: 1,
            username: 'admin',
            password: 'htic2025',
            name: 'Administrator'
        }
    ]
};
fs.writeFileSync(ADMINS_FILE, JSON.stringify(admins, null, 2));
console.log('   Da tao tai khoan: admin / htic2025');

console.log('');
console.log('========================================');
console.log('   KHOI TAO HOAN TAT!');
console.log('========================================');
console.log('');
console.log('   Cac file da tao:');
console.log('   - data/articles.json');
console.log('   - data/contacts.json');
console.log('   - data/admins.json');
console.log('');
console.log('   Buoc tiep theo: npm start');
console.log('');