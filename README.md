# Draw Music Studio — Terms & Privacy

Tài liệu tiếng Anh cho **Draw Music Studio**, package `com.khoaidev.drawmusic`, version 1.0.0, nhà phát triển KhoaiStore, email hvdevelopapplication@gmail.com. Đối chiếu mã nguồn và merged release manifest ngày 02/11/2026. Package cũ `com.drawmusic.studio` trên website đã được thay để khớp applicationId/namespace hiện tại của Android.

- Privacy: https://hoangvietonline.github.io/Draw_Music_Privacy_Policy/
- Terms: https://hoangvietonline.github.io/Draw_Music_Privacy_Policy/terms.html
- GitHub: https://github.com/hoangvietonline/Draw_Music_Privacy_Policy

## Repo độc lập trong project

Thư mục `Draw Music Legal/` nằm trong project Draw Music nhưng có `.git` riêng và được repo Android bỏ qua. Chỉ commit/push từ thư mục này để cập nhật website. GitHub Pages dùng main, thư mục gốc.

## Đóng gói

Chạy `python3 sync_offline.py` từ thư mục này sau khi sửa nội dung. Script nhúng CSS và sao chép hai trang vào assets `privacy-local.html`, `terms-local.html`. Android tự đóng gói các assets vào APK/AAB. Settings có hai mục Privacy và Terms riêng: ưu tiên URL GitHub Pages, tự chuyển sang bản đóng gói nếu lỗi mạng, lỗi HTTP hoặc tải quá 5 giây. Bản mặc định dùng Internet để tải trang pháp lý; nội dung sáng tác vẫn xử lý trên máy. Google Ads/UMP có thể dùng mạng nếu được bật trong bản phát hành khác. Không cần mạng để đọc hai tài liệu.

## Phạm vi

Mô tả app hiện tại: local projects/Room, DataStore, background photo qua picker hoặc camera app bên ngoài, ảnh nhúng JSON, WAV/MIDI/MP4, xuất/chia sẻ, retention/deletion; không login, SDK analytics riêng hoặc billing; allowBackup=false. Google Mobile Ads Next-Gen và UMP đã tích hợp nhưng `admob.enabled=false`, không khởi tạo hoặc yêu cầu consent/quảng cáo ở bản mặc định, chưa có vị trí hiển thị quảng cáo. Privacy mô tả riêng trạng thái này và các quyền được SDK khai báo trong merged manifest. Trước khi bật SDK hoặc thêm vị trí quảng cáo phải cập nhật policy và Data safety theo bản phát hành thực tế.

Tên nhà phát triển/email dùng thông tin KhoaiStore đã có trong bộ tài liệu tham chiếu cùng chủ tài khoản; đối chiếu với store listing khi phát hành. Chưa kiểm tra cấu hình Play Console hoặc lưu lượng của AAB cuối cùng.

Nguồn chính thức: [Google Play User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en), [Android backup](https://developer.android.com/identity/data/autobackup), [GitHub privacy](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
